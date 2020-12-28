n,k = [int(x) for x in input().split()]
array = [int(x) for x in input().split()]
if k==0:
    for x in array:
        print(x,end=' ')
else:
    if k%2==0:
        m = max(array)
        for y in range(n):
            array[y]=m-array[y]
    n = max(array)
    for x in array:
        print(n-x,end=' ')