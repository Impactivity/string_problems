import sys

read = sys.stdin.readline
n = sorted( list(read().rstrip()) , reverse=True)
_sum = 0

if '0' not in n:
    print(-1)
    exit(0)

for num in n:
    _sum += int(num)

if _sum % 3 == 0:
    print(''.join(n))
else:
    print(-1)




#
# #
# read = sys.stdin.readline
# temp = list(map(str, read().rstrip()))
#
# max_num = sorted( temp, reverse= True)
# min_num = sorted(temp , reverse = False)
#
# start = int(''.join(min_num))
# end = int(''.join(max_num))
# answer = -1
#
# if end % 30 == 0 :
#     print(end)
#     exit(0)
#
#
# def check(number):
#     arr = set(map(str, str(mid).rstrip()))
#     if len(arr & set(temp)) != len(arr) :
#             return False
#     return True
#
# while start <= end:
#     mid = (start + end) // 2
#     print(mid)
#     if mid % 30 == 0:
#         if check(mid):
#             answer = mid
#             start = start + 1
#         else:
#             start = start + 1
#     elif mid % 30 != 0:
#         start = mid + 1
#
# print(answer)







