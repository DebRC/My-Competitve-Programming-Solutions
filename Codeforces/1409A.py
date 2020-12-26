# your code goes here
import math
for _ in range(int(input())):
    a,b=map(int, input().split())
    res=abs(a-b)
    print(math.ceil(res/10))