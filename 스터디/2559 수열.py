import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
tmp = sum(arr[:m])
ans = tmp
for i in range(m,n):
    tmp +=arr[i]
    tmp -= arr[i-m]
    if tmp>ans:
        ans = tmp
print(ans)
# 132ms
# N, K = map(int, input().split())
# arr = list(map(int, input().split()))
# tmp = sum(arr[:K])
# result = tmp
# for i in range(K, N):
#     tmp += arr[i] - arr[i-K]
#     result = max(result, tmp)
# print(result)

# 136ms
# N, K = map(int, input().split())
# tem_list = list(map(int, input().split()))
#
# part_sum = sum(tem_list[:K])
# result_list = [part_sum]
#
# for i in range(0, len(tem_list)-K):
#     part_sum = part_sum - tem_list[i] + tem_list[i+K]
#     result_list.append(part_sum)
#
# print(max(result_list))

# 144ms
# N, K = map(int, input().split())
# tem_list = list(map(int, input().split()))
# i = 0
# part_sum = sum(tem_list[:K])
# result_list = part_sum
# if K == 1:
#     print(max(tem_list))
# else:
#     while 1:
#         part_sum -= tem_list[i]
#         if i+K >=N:
#             break
#         part_sum += tem_list[i+K]
#         if result_list<part_sum:
#             result_list=part_sum
#         i+=1
#     print(result_list)