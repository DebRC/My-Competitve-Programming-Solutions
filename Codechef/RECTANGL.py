# cook your dish here
# cook your dish here
for _ in range(int(input())):
    a=list(map(int, input().split()))
    if((a[0]+a[1]==a[2]+a[3]) or (a[0]+a[2]==a[1]+a[3]) or (a[0]+a[3]==a[1]+a[2])):
        print("YES")
    else:
        print("NO")