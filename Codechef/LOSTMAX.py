# cook your dish here
for _ in range(int(input())):
    a=list(map(int, input().split()))
    n=len(a)-1
    if n in a:
        a.remove(n)
    print(max(a))