import sys
import re
read = sys.stdin.readline
patern = re.compile(r'<[/a-zA-z\s\w\r"=(http(s?)\:\/\/.)]+>')
while True:
    textline = read().rstrip()
    if textline == '#':
        break

    arr = patern.findall(textline)

    stack = []

    for i in range(len(arr)):
        if len(stack) >= 1 :
            if stack[-1][0:] == arr[i][2:-1]:
                stack.pop()
            elif arr[i][1:3] == '/a' and arr[i][2] == stack[-1][0]:
                stack.pop()
            else:
                if arr[i][-2] == '/':
                    continue
                stack.append(arr[i][1:-1])
        else:
            if arr[i][-2] == '/' :
                continue
            else:
                stack.append(arr[i][1:-1])

    if len(stack) == 0:
        print('legal')
    else:
        print('illegal')

