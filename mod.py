#!/usr/bin/python

import sys

if len(sys.argv) == 3:
    print('{} mod {} = {}'.format(sys.argv[1], sys.argv[2], pow(int(sys.argv[1]), 1, int(sys.argv[2]))))
else:
    print('\n\nUsage:   mod.py <number> <modulo>\n')
