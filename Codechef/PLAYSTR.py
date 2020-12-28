# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=list(input())
    r=list(input())
    s1=s.count("1")
    r1=r.count("1")
    if(s1==r1):
        print("YES")
    else:
        print("NO")