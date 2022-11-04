n, d = list(map(int,input().split()))
ansNum = 0
ans = 0
for i in range(n):
    s1, s2, s3 = list(map(int,input().split()))
    if abs(s1 - s2) >= d or abs(s2 - s3) >= d or abs(s1 - s3) >= d:
        ans += (s1+s2+s3)/3
        ansNum += 1

print(ansNum, end=" ")
print(int(ans))
