#!/usr/bin/python

import sys

if (len(sys.argv) == 3 or len(sys.argv) == 4) and sys.argv[1] == '-n':
    print(pow(int(sys.argv[2]), 2))
elif len(sys.argv) == 4:
    print('\npow({}, {}, {}) = {}'.format(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), pow(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))))
elif len(sys.argv) == 3:
    print('\npow({}, {}) = {}'.format(int(sys.argv[1]), int(sys.argv[2]), pow(int(sys.argv[1]), int(sys.argv[2]))))
else:
    print('\n\nUsage:   pow.py <base> <power>')
    print('         pow.py <base> <power> <modulo>')

