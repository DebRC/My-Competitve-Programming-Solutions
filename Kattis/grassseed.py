c=float(input())
n=int(input())
add=0
for i in range(n):
    l,b=map(float, input().split())
    add+=(l*b)
print(c*add)