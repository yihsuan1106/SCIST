a1, b1, c1 = list(map(int,input().split()))
a2, b2, c2 = list(map(int,input().split()))
n = int(input())
nn = 0
nnn = n
ans = a1*nnn*nnn + b1*nnn + c1 + a2*nn*nn + b2*nn + c2
while nn != n+1:
    y1 = a1*nnn*nnn + b1*nnn + c1
    y2 = a2*nn*nn + b2*nn + c2
    if ans < y1+y2:
        ans = y1+y2
    nn += 1
    nnn -= 1
print(ans)
