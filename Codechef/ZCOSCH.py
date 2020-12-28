# cook your dish here
rank=int(input())
if(rank<=50 and rank>=1):
    print("100", end="")
elif(rank<=100 and rank>=51):
    print("50", end="")
else:
    print("0")