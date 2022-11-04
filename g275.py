num = int(input())
for i in range(num):
    none = 0
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if a[1] == a[3] or a[1] != a[5] or b[1] == b[3] or b[1] != b[5]:
        print('A', end="")
        none = 1
    if a[6] != 1 or b[6] != 0:
        print('B', end="")
        none = 1
    if a[1] == b[1] or a[3] == b[3] or a[5] == b[5]:
        print('C', end="")
        none = 1
    if none == 0:
        print("None")
    if none != 0:
        print() 
