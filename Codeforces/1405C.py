for _ in range(int(input())):
	n, k = map(int, input().split())
	s = input()
	x = y = 0
	for i in range(k):
		a = b = 0
		for j in range(i, n, k):
			if s[j] == '1':
				a += 1
			elif s[j] == '0':
				b += 1
		if min(a, b) > 0:
			print('NO')
			break
		if a:
			x += 1
		elif b:
			x -= 1
		else:
			y += 1
	else:
		if abs(x) <= y:
			print('YES')
		else:
			print('NO')
		
	