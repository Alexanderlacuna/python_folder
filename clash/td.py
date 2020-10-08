def weird(n):
	s=[]
	while n!=1:
		s.append(str(n))
		if n%2==0:

			n=n//2
		else:
			n=(n*3)+1
	s.append(str(n))
	print(" ".join(s))


def missing(num,vals):
	f=list(sorted(vals))
	for i in range(1,f[-1]+1):
		if i not in f:
			print(i)
			break



n=int(input())
weird(n)
missing(5,[2,3,1,5])

