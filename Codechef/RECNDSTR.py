t=int(input())
while(t>0):
    string=input()
    if (len(string)==1 or len(string)==2):
        print("YES")
    else:
        l=string[1:]+string[0]
        r=string[len(string)-1]+string[:len(string)-1]
        if(l==r):
            print("YES")
        else:
            print("NO")
    t-=1