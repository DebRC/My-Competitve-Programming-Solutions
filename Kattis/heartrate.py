for _ in range(int(input())):
    b,p=map(float, input().split())
    bpm=60*(b/p)
    prec=60/p
    print("%.4f"%(bpm-prec),"%.4f"%(bpm),"%.4f"%(bpm+prec))