for _ in range(int(input())):
    s1=list(input())
    s2=list(input())
    n=len(s1)
    min_diff=0
    max_diff=0
    for i in range(n):
        if s1[i]!=s2[i] and s1[i]!='?' and s2[i]!='?':
            min_diff+=1
            max_diff+=1
        if s1[i]=='?' or s2[i]=='?':
            max_diff+=1
    print(min_diff,max_diff)