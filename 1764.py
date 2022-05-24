import sys
read = sys.stdin.readline

n,m = map(int,read().split())

not_listen = set()
not_seen = set()

for _ in range(n):
    not_listen.add(read().rstrip())

for _ in range(m):
    not_seen.add(read().rstrip())

answer = sorted(list(not_listen & not_seen))
print(len(answer))
for name in answer:
    print(name)