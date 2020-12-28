for _ in range(int(input())):
    n=list(map(int, input()))
    if n.count(0)>n.count(1):
        print("LOSE")
    else:
        print("WIN")