# cook your dish here
for _ in range(int(input())):
    char=input()
    if char=='B' or char=='b':
        print('BattleShip')
    elif char=='C' or char=='c':
        print('Cruiser')
    elif char=='D' or char=='d':
        print('Destroyer')
    elif char=='F' or char=='f':
        print('Frigate')