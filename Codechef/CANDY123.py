for _ in range(int(input())):
    a,b=map(int, input().split())
    i=1
    while(1):
        if(i%2!=0):
            a-=i
        else:
            b-=i
        if(a<0 or b<0):
            break
        i+=1
    if(a<0):
        print("Bob")
    else:
        print("Limak")