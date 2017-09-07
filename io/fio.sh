#!/bin/bash

# Run fio with a bunch of different options to test a filesystems performance

dir=${1}
logdir=`readlink -f ${2}`

mkdir -p ${logdir}

size=20G

# First run various block sizes
pushd ${dir} 2>&1 > /dev/null
for blocksize in 4 32 64 128 256 512; do
    # then loop through various read/write combinations
    for rwmix in 25 50 75; do
        echo "${blocksize}k-${rwmix}"
        fio --randrepeat=1 \
            --ioengine=libaio \
            --direct=1 \
            --gtod_reduce=1 \
            --name=test \
            --filename=test \
            --bs=${blocksize}k \
            --iodepth=64 \
            --size=${size} \
            --readwrite=randrw \
            --rwmixread=${rwmix} \
            2>&1 | tee > ${logdir}/${blocksize}k-${rwmix}.log
        echo "done\n"
    done
done

popd 2>&1 > /dev/null
