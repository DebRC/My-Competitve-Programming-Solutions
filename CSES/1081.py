def maxgcdpair(arr,n):
    high = max(arr)
    divisors= [0]*(high+1)
    for i in range(0,n):
        divisors[arr[i]]+=1
    counter = 0
    for i in range(high,0,-1):
        for j in range(i,high+1,i):
            if divisors[j]>0:
                counter+=divisors[j]
            if counter==2:
                return i
        counter=0
    return high
n=int(input())
arr=list(map(int, input().split()))
print(maxgcdpair(arr,n))