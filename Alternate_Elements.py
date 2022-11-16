for i in range(int(input())):
    x=list(map(int,input().split()))
    y=x[1:(x[0]+1)]
    for j in range(0,len(x)):
        if j%2==1:
            print(x[j],end=" ")
    print()