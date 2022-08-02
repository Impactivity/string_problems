import re
import sys
read = sys.stdin.readline
inp = read().rstrip()
p = re.fullmatch(r'(100+1+|01)+',inp)

if p is None:
    print('NOISE')
else:
    print('SUBMARINE')

