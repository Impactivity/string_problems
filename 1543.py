import sys
import re

read = sys.stdin.readline

src = read().rstrip()
find = read().rstrip()

p = re.findall(find,src)
print(len(p))
