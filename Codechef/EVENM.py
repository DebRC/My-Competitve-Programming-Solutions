# cook your dish here
for _ in range(int(input())):
    n=int(input())
    N=0
    if (n%2!=0):
        for i in range(n):
            for j in range(n):
                N+=1
                print(N, end=" ")
            print()
    else:
        for i in range(n):
            if i%2==0:
                for j in range(n):
                    N+=1
                    print(N, end=" ")
                print()
            else:
                N+=n
                for j in range(n):
                    print(N, end=" ")
                    N-=1
                N+=n
                print()
                    