t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))[:n]
    cursum=0
    orisum=0
    for i in range(n):
        orisum+=arr[i]

    for i in range(n):
        if arr[i]>k:
            arr[i]=k
            cursum+=arr[i]
        elif arr[i]<=k:
            cursum+=arr[i]

    print(abs(orisum-cursum))
