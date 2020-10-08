def binary_search(arri,search_item):
	arri=sorted(arri)
	start=0
	end=len(arri)-1
	index=None

	while (start<=end ):
		mid=((start+end)//2)
		print(mid)

		if (arri[mid]==search_item):
			index=mid
			break

		else:
			if (arri[mid]>search_item):
				end=mid-1

			else:
				start=mid+1


	return index

def linear_search(arri,search_item):
	start=0
	found=None
	for index,num in enumerate(arri):
		print(num,index)
		if num==search_item:
			print(f"the index is {index}")
			found=index
			break

	return found



numbers=range(1,10000)
print(binary_search(numbers,1200))
print(linear_search(numbers,1200))

