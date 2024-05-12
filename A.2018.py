n = int(input())
a = list(map(int, input().split()))
a.sort()
cnt = 0
mcnt = 0
c = a[0]
for i in range(len(a) - 1):
    if a[i] == a[i+1]:
        cnt += 1
        if mcnt <= cnt:
            mcnt = cnt
            c = a[i]
    else:
        cnt = 0
print(f"{c}")