n=int(input())
total=0
max_total=0
for i in range(n):
    a,b=map(int, input().split())
    total=total-a+b
    if total>max_total:
        max_total=total
print(max_total)