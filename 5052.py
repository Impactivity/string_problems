import sys

read = sys.stdin.readline

def check():
    for i in range(len(number_list) - 1):
        if number_list[i] == number_list[i+1][0:len(number_list[i])]:
            print('NO')
            return
    print('YES')


t = int(read())
for _ in range(t):
    n = int(read())
    number_list = []
    for _ in range(n):
        number_list.append(read().rstrip())

    number_list.sort()
    check()

