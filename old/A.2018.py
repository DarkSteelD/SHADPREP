from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
count = defaultdict(int)
max_count = 0
max_num = 0
for num in a:
    count[num] += 1
    if count[num] > max_count or (count[num] == max_count and num > max_num):
        max_count = count[num]
        max_num = num

print(max_num)
