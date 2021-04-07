import functions
import sys

if len(sys.argv) == 2:
    print(functions.find_divisors(int(sys.argv[1])))
else:
    print('Usage finddiv.py <number>')
