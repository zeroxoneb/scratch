#!/usr/bin/env python3

import subprocess
import sys


def myrun(cmd):
    """
    from http://blog.kagesenshi.org/2008/02/teeing-python-subprocesspopen-output.html
    """
    cmd = cmd.split(" ")
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
        stdout = []
        line = str(proc.stdout.readline().strip().decode('utf-8'))
        while line:
            stdout.append(line)
            print(line)
            line = str(proc.stdout.readline().strip().decode('utf-8'))

    return ''.join(stdout)

if __name__ == '__main__':
    stdout = myrun(sys.argv[1])
    print(stdout)
