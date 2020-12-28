# cook your dish here
t=int(input())
while(t>0):
    base=float(input())
    if(base<1500):
        print('%.2f'%(base+(0.1*base)+(0.9*base)))
    else:
        print('%.2f'%(base+500+(0.98*base)))
    t-=1