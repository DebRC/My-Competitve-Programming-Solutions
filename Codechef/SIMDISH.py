# cook your dish here
for _ in range(int(input())):
    s1=list(input().split())
    s2=list(input().split())
    c=0
    for i in s1:
        if i in s2:
            c+=1
    if(c>=2):
        print("similar")
    else:
        print("dissimilar")