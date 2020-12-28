# cook your dish here
for _ in range(int(input())):
    a=list(input())
    count=0
    for i in range(0,len(a),2):
        if (a[i]=="A" and a[i+1]=="B"):
            count+=1
        elif (a[i]=="B" and a[i+1]=="A"):
            count+=1
        else:
            break
        #print(count)
    if(count==(len(a)//2)):
        print("yes")
    else:
        print("no")