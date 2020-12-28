# cook your dish here
for _ in range(int(input())):
    s=input()
    count=0
    h=0
    for i in s:
        for j in s:
            #print(i,j)
            if i==j:
                count+=1
        #print(count)
        if count>h:
            h=count
        count=0
    #print(h)
    if (2*h==len(s)):
        print("YES")
    else:
        print("NO")