a=list(map(float, input().split()))
withdraw=a[0]
balance=a[1]
if(withdraw+0.5<=balance and withdraw<=2000 and withdraw%5==0):
    balance=balance-withdraw-0.5
print("%.2f"%balance)