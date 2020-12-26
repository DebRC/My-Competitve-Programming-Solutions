province=8
duchy=5
estate=2
gold=6
silver=3
copper=0
g,s,c=map(int, input().split())
power=g*3+s*2+c*1
temp=[]
if power>=province:
    temp.append("Province")
elif power>=duchy:
    temp.append("Duchy")
elif power>=estate:
    temp.append("Estate")
if power>=gold:
    temp.append("Gold")
elif power>=silver:
    temp.append("Silver")
elif power>=copper:
    temp.append("Copper")
print(" or ".join(temp))