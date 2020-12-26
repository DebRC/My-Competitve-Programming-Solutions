y,p=input().split()
y=list(y)
p=list(p)
n=len(y)
if y[n-2]=="e" and y[n-1]=="x":
    new=y+p
elif y[n-1]=="a" or y[n-1]=="e" or y[n-1]=="i" or y[n-1]=="o" or y[n-1]=="u":
    new=y[:n-1]+["e","x"]+p
else:
    new=y+["e","x"]+p
print("".join(new))