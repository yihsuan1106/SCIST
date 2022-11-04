while(1):
    try:
        a1 = int(input()) 
        a2 = list(map(int,input().split()))
        a2.sort()
        for i in a2:
            print(i, end = " ")
        print()
    except:
        break
