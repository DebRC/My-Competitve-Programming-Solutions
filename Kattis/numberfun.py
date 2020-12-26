for _ in range(int(input())):
    a,b,c=map(float, input().split())
    flag=0
    if (a+b==c) or (a*b==c) or (a-b==c) or (b-a==c) or (a/b==c) or (b/a==c):
        print("Possible")
    else:
        print("Impossible")