# def findMin(arri,low,high):
# 	if high<low:
# 		return arri[0]
# 	if high==low:
# 		return arri[low]
# 	mid=((low+high)/2)

# try:
# 	pass
# except Exception as e:
# 	raise e
def merge(arri):
	print(arri)
	if len(arri)>1:
		mid=len(arri)//2
		lefthalf=arri[:mid]
		righthalf=arri[mid:]
		merge(lefthalf)
		merge(righthalf)

	i=j=k=0
	while i<len(lefthalf) and j<len(righthalf):
		if lefthalf[i]<righthalf[j]:
			arri[k]=lefthalf[i]
			i+=1
			print(arri)
		else:
			arri[k]=lefthalf[j]
			j+=1
			print(arri)

		k+=1

	while i<len(lefthalf):
		arri[i]=lefthalf[i]
		i+=1
		k+=1
	while j<len(righthalf):
		arri[j]=righthalf[j]
		j+=1
		k+=1
	return arri

	
	# end=len(arri)-1
	
	


def bubble(arri):
	start=0
	while arri!=sorted(arri):
		print(arri)
		if arri[start]>arri[start+1]:
			temp=arri[start]
			arri[start]=arri[start+1]
			arri[start+1]=temp
		start=(start+1)%(len(arri)-1)
	return arri

def swap(arri,left,right):
	print("Executing")
	temp=arri[left]
	arri[left]=arri[right]
	arri[right]=temp
	return arri
def sorting(arri):
	left=0
	right=0
	pivot=len(arri)//2
	while left<right:
		if arri[left]>arri[pivot] and arri[right]<arri[pivot]:

			swap(arri,left,right)
			left+=1
			right-=1

		
		

	return arri

