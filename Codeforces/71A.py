for _ in range(int(input())):
    s=list(input())
    if len(s)<=10:
        print(''.join(s))
    else:
        print(s[0]+str(len(s)-2)+s[len(s)-1])