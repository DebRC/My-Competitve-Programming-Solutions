n=int(input())
total=n*(n+1)//2
if total&1:
	print("NO")
	exit(0)
total=total//2
print("YES")
if n&1:
	set1=[]
	set2=[]
	for i in range(n,0,-1):
		if total>=i:
			set1.append(i)
			total-=i
		else:
			set2.append(i)
	print(len(set1))
	set1.reverse()
	print(*set1)
	set2.reverse()
	print(len(set2))
	print(*set2)
else:
	print(n//2)
	for i in range(2,n//2+1,2):
		print(i,end=" ")
	for i in range(n//2+1,n+1,2):
		print(i,end=" ")
	print()
	print(n//2)
	for i in range(1,n//2+1,2):
		print(i,end=" ")
	for i in range(n//2+2,n+1,2):
		print(i,end=" ")