# cook your dish here
for _ in range(int(input())):
    s=list(input())
    n=len(s)
    pair=0
    for i in range(n):
        if s[i]=='<':
            s[i]='>'
        elif s[i]=='>':
            s[i]='<'
    #print(s)
    for i in range(n-1):
        if s[i]=='>' and s[i+1]=='<':
            pair+=1
    print(pair)