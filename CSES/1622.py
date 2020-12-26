def toString(List): 
    return ''.join(List)
def permute(a, l, r,arr): 
    if l==r: 
        arr.append(toString(a)) 
    else: 
        for i in range(l,r+1): 
            a[l],a[i]=a[i],a[l] 
            permute(a, l+1, r,arr) 
            a[l], a[i] = a[i], a[l] 
a=list(input())
arr=[]
permute(a,0,len(a)-1,arr)
arr.sort()
arr=sorted(set(arr))
print(len(arr))
for i in arr:
    print(i)