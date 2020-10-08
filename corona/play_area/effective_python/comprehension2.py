matrix=[[1,2,3,4],[8,5,3,2]]
li=[x for row in matrix for x in row ]

sqauared=[[x**2 for x in row] for row in matrix]

square2=[row for row  in matrix]
for item in square2:
	print(item)
print(sqauared)
print(square2)



def find_sum(arri,target):
	arri=sorted(arri)
	low=0
	high=len(arri)-1
	found=False
	while(low<high):
		print(high,low)
		dum=arri[high]+arri[low]
		print(dum)

		if dum==target:

			found =True
			break

		else:
			high-=1
			low+=1


	return found


def find_sum2(arri,target):
	s=set()

	found=False

	diff=0
	for num in arri:
		print(s)
		diff=target-num
		# print(diff)


		if num in s:
			print("ASd")
			found=Tru
			break

		else:
			s.add(diff)



	return found



d=[1,2,3,4,5,6,7]
s=find_sum(d,8)
print(s)

print(find_sum2(d,15))
		



