s=list(input())
i=0
while(i<len(s)):
    if s[i]==".":
        print(0,end="")
        i+=1
    elif s[i]=="-" and s[i+1]==".":
        print(1,end="")
        i+=2
    elif s[i]=="-" and s[i+1]=="-":
        print(2,end="")
        i+=2