# cook your dish here
for _ in range(int(input())):
    s1=input()
    s2=input()
    n=len(s1)
    flag=0
    for i in range(n):
        if(s1[i]==s2[i]):
            continue
        elif((s1[i]=='?' and s2[i]!='?') or (s1[i]!='?' and s2[i]=='?')):
            continue
        elif(s1[i]!=s2[i]):
            print("No");
            flag=1;
            break;
    if(flag==0):
        print("Yes")