def f(a,b):
    M=max(a,b)
    return (a-b)*(-1)**M+M*M-M+1
    
for _ in range(int(input())):
    y,x=map(int, input().split())
    print(f(y,x))