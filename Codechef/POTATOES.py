# cook your dish here
def isprime(n):
    if n==1 or n==0:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return False
        return True
for _ in range(int(input())):
    x,y=map(int, input().split())
    i=1
    while(isprime(x+y+i)==False):
        i+=1
    print(i)