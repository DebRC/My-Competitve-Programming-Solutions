def check(n):
    total=0
    while(n>0):
        total+=n%10
        n//=10
    return total
while(1):
    n=int(input())
    if n==0:
        break
    i=11
    #print(check(n))
    while(check(n)!=check(n*i)):
        i+=1
    print(i)