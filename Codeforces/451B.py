import sys
n=int(input())
a=list(map(int, input().split()))
flag=1
for i in range(n-1):
    if(a[i] > a[i + 1]):
        flag = 0
        front = i
        break
if flag:
    print("yes")
    print("1 1")
    sys.exit()
end=front
while(end<n-1 and a[end]>a[end+1]):
    end+=1
a[front:end+1]=reversed(a[front:end+1])
if a==sorted(a):
    print("yes")
    print(front+1,end+1)
else:
    print("no")