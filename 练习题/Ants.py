num=int(input())
for i in range(num):
    l,n=map(int,input().split())
    ants=list(map(int,input().split()))
    x=[]
    y=[]
    for j in list(ants):
        if j>=l/2:
            x.append(l-j)
        else:
            x.append(j)
    for k in list(ants):
        if k>=l/2:
            y.append(k)
        else:
            y.append(l-k)
    print(max(x),max(y))