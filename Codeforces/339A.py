a=list(map(int, input().split('+')))
a.sort()
a=[str(x) for x in a]
print('+'.join(a))