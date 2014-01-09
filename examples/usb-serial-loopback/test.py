#!/usr/bin/python

import sys
from serial import Serial
from time import sleep

test = 'hello world\n' 
def ping(s):
        s.write(test)
        r = s.readline()
        if r != test:
                #print 'uh oh:', test.encode('string_escape'), r.encode('string_escape')
                pass
        sys.stdout.write('.')
        sys.stdout.flush()

count = 0
while True:
        s = Serial('/dev/ttyACM0')
        ping(s)
        #sys.stdout.write('%d\r' % count)
        #sys.stdout.flush()
        count += 1
        sleep(1)
        s.close()
