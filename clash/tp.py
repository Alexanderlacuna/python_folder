
b=[]
def sums(arri,target):
	for val in arri:
		curr=val
		w=True
		while (w):

			diff=target-curr
			if diff in arri:
				print("the diff is",diff)
				print("curr is",curr)
				print("yes it is")
				if ([diff,curr] in b):
					w=False
				else:


					b.append([diff,curr])
					curr=diff
			else:
				

				if diff>0:
					print("yes diff is greater",diff)
					curr=diff
				else:
					print("am breaking")
					w=False
					break

	return b
