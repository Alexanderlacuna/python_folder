multi=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

i=len(multi)-1
j=0

arri=[]
# while i>=0:
# 	while j<=(len(multi)-1):
# 		arri[i][j]=multi[j][i]

# 		j+=1


# 	i-=1



def  rotate_90_deg_clockwise(matrix):
	new_matrix=[]
	for i in range(len(matrix[0])):
		li=list(map(lambda x:x[i],matrix))
		# li.reverse
		new_matrix.append(li)





	return new_matrix

	



	

print(multi)

ari=[[1,2],[3,4]]

for i in range(len(ari[0])):
	print(len(ari)-1)
	print(i)

	l=list(map(lambda x:x[i],ari))
	print(f'the index value  is {i}')
	print(f"the value of l is {l}")
s=rotate_90_deg_clockwise(multi)
print(s)