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

# def recursive_function(i):
#     if i == 100:
#         return
#     print(i, '번째 재귀 함수에서', i + 1, '번째 재귀함수를 호출합니다.')
#     recursive_function(i+1)
#     print(i,'번째 재귀함수를 종료합니다.')
#
# recursive_function(1)

# def recusive_function(i):
#     if i <= 1:
#         return 1
#     return recusive_function(i-1) * i
#
# n = int(input())
# print(recusive_function(n))

# n, k = map(int, input().split())
# a = map(int,input().split())
# b = map(int,input().split())
# max = 0
# max_list = []

# from bisect import bisect_left, bisect_right
#
# a = [1,2,4,4,8]
# x = 4
#
# print(bisect_left(a,x))
# print(bisect_right(a,x))

# from bisect import bisect_left, bisect_right
#
# num = int(input())
# num_list = map(int, input().split())
#
# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, left_value)
#     left_index = bisect_left(a, right_value)
#     return right_index -  left_index
#
# a = [1,2,3,3,3,3,4,4,8,9]
# print(count_by_range(a, 4,4,))
# print(count_by_range(a, -1, 3))
# import bisect
#
# from bisect import bisect_left, bisect_right
#
# a, b = map(int,input().split())
# num_list = list(map(int, input().split()))
#
# print(bisect.bisect_right(num,num_list) - bisect_left(num,num))

