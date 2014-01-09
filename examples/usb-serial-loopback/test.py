#!/usr/bin/python

import sys
from serial import Serial

test = 'hello world\n' 
count = 0
while True:
        s = Serial('/dev/ttyACM0')
        s.write(test)
        r = s.readline()
        if r != test:
                print r
        sys.stdout.write('%d\r' % count)
        count += 1
        s.close()
