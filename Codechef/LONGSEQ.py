# cook your dish here
for _ in range(int(input())):
    n=list(map(int, input()))
    if(n.count(0)==1 or n.count(1)==1):
        print("Yes")
    else:
        print("No")