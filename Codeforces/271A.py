def check(n):
    n=[str(x) for x in str(n)]
    if len(n)==len(set(n)):
        return True
    return False
n=int(input())
flag=False
while(flag!=True):
    n+=1
    flag=check(n)
print(n)