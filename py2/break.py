#!/usr/bin/env python2

# Example using break and for/else semantics where the inner loop breaks when
# it has found that x == y.
for x in range(10):
    for y in range(10):
        print('x:{},y:{}'.format(x, y))

        # if x and y are both 5 then break out of the loop
        if x == y:
            print('break->x:{},y:{}'.format(x, y))
            break

    # This is called when the break condition is *not* met during the loop
    else:
        print('inner for/else->x:{},y:{}'.format(x, y))

# This is called at the end of the inner loop because there is no break called
# during the inner loop
else:
    print('outer for/else->x:{},y:{}'.format(x, y))
