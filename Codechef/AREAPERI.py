# cook your dish here
length=int(input())
breadth=int(input())
area=length*breadth
peri=2*(length+breadth)
if area>peri:
    print('Area')
    print(area)
elif peri>area:
    print('Peri')
    print(peri)
else:
    print('Eq')
    print(area)