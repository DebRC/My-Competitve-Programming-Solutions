def expo(n):
    rem=n%10
    n=n//10
    return n,rem
total=0
for _ in range(int(input())):
    n,rem=expo(int(input()))
    total+=(n**rem)
print(total)