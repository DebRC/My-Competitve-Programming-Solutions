# cook your dish here
t=int(input())
while(t>0):
    t-=1
    s=input()
    pair=0
    i=0
    while(i<len(s)-1):
        if((s[i]=='x' and s[i+1]=='y') or (s[i]=='y' and s[i+1]=='x')):
            pair+=1
            i+=2
        else:
            i+=1
    print(pair)