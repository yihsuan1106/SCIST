a  = int(input())
a1 = list(map(int,input().split()))
ans = 0
for i in range(len(a1)):
    if(a1[i] == 0):
        if(i == 0):
            ans += a1[i+1]
        elif(i == len(a1)-1):
            ans += a1[i-1]
        else:
            if(a1[i-1] < a1[i+1]):
                ans += a1[i-1]
            else:
                ans += a1[i+1]

print(ans)
