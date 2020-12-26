def maximum(a,n):
    max_ele=0
    max_index=0
    for i in range(n):
        if a[i]>max_ele:
            max_ele=a[i]
            max_index=i
    return max_index
def minimum(a,n):
    min_ele=101
    min_index=0
    for i in range(n):
        if a[i]<=min_ele:
            min_ele=a[i]
            min_index=i
    return min_index
n=int(input())
a=list(map(int, input().split()))
max_index=maximum(a,n)
min_index=minimum(a,n)
if max_index<min_index:
    print(max_index+n-1-min_index)
else:
    print(max_index+n-1-min_index-1)