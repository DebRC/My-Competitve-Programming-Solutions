a=[2]*1000001
a[1]=1
def sieve():
    for i in range(2,int(pow(1000001,0.5))+1):
        for j in range(i*i,1000001,i):
            if j//i==i:
                a[j]+=1
            else:
                a[j]+=2
sieve()
for _ in range(int(input())):
    print(a[int(input())])