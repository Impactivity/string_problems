import sys
import re

read = sys.stdin.readline

p = re.compile('(100+1+|01)+')

n = int(read())
for _ in range(n):
    arr = p.fullmatch(read().rstrip())
    if arr is None:
        print('NO')
    else:
        print('YES')
