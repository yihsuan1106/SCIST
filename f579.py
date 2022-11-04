a, b = list(map(int,input().split()))
people = int(input())
ans = 0
for ii in range(people):
    aa = 0; bb = 0
    s = list(map(int,input().split()))
    for i in s:
        if i == a:
            aa += 1
        elif i == -a:
            aa -= 1
        if i == b:
            bb += 1
        elif i == -b:
            bb -= 1
    if aa > 0 and bb > 0:
        ans += 1
print(ans)
