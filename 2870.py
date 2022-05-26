import re
import sys

read = sys.stdin.readline

n = int(read())
arr = [read().split() for _ in range(n)]
answer = []

for str in arr:
    p = re.findall('[0-9]+', str[0])
    p = list(map(int,p))
    answer += p

answer.sort()

for num in answer:
    print(num)

