n, d = list(map(int,input().split()))
a = list(map(int,input().split()))
temp = a[0]; ans = 0
stock = 1
for i in a:
    if i >= temp + d and stock == 1:
        ans += (i - temp)
        temp = i - d
        stock = 0
    if i <= temp and stock == 0:
        temp = i
        stock = 1

print(ans)
