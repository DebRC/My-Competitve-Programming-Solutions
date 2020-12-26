for _ in range(int(input())):
    a=input()
    b=input()
    print(a)
    print(b)
    a=list(a)
    b=list(b)
    n=len(a)
    for i in range(n):
        if a[i]==b[i]:
            print(".",end="")
        else:
            print("*",end="")
    print("\n")