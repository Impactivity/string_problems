import sys
read = sys.stdin.readline

input_string = read()


# solution 1
# if len(input_string) % 10 == 0:
#     n = len(input_string) // 10
# else:
#     n = len(input_string) // 10 + 1
#
# for i in range(0,n):
#     st = i * 10
#     ed = i * 10 + 10
#     print(input_string[st:ed])



# solution 2
for i in range(0,len(input_string),10):
    print(input_string[i:i+10])