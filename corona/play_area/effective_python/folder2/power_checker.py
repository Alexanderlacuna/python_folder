n=1000

results={}


for a in range(3,1001):
	for b in range(3,1001):
		results[(a**3)+(b**3)]=(a,b)


for c in range(3,1001):
	for d in range(3,1001):
		if (((c**3) +(d**3)) in results):
			# results.get((c**3+d**3))
			print(results[(c**3+d**3)])
			break

	break