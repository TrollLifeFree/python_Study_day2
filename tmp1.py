# dx = [0,-1,0,1]
# dy = [1,0,-1,0]
# cp = [0,0]
#
# n = int(input())
# list = input().split()
#
# for i in list:
#     if i == 'D':
#         cp[0] += dx[0]
#         cp[1] += dy[0]
#         if cp[1] > n - 1:
#             n -= 1
#     elif i == 'L':
#         cp[0] += dx[1]
#         cp[1] += dy[1]
#         if cp[0] < 0:
#             n = 0
#     elif i == 'U':
#         cp[0] += dx[2]
#         cp[1] += dy[2]
#         if cp[1] < 0:
#             n = 0
#     elif i == 'R':
#         cp[0] += dx[3]
#         cp[1] += dy[3]
#         if cp[0] > n - 1:
#             n -= 1
#     else:
#         print("Error")
#         break
#     print(cp[0], cp[1], end=" ")
#
# #print(cp[0], cp[1], end=" ")
