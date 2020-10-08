numbers=[3,1,4,5,8,9,6,5,23,76]
numbers=sorted(numbers)
print(numbers)
number_search=6

count=0
# while num !=number_search and count<0:s


start=0
end=len(numbers)
guess=6



while count<=len(numbers):
	midpoint=((start+end)//2)


	if guess==numbers[start] or guess==numbers[end-1]:
		print(f"easy target index is either {start} {end-1}")
		break

	# elif int(num)
	
	elif numbers[midpoint]==guess:
		print(f"the number index is {midpoint}")
		break

	elif guess>numbers[midpoint]:
		start=midpoint

	elif guess<numbers[midpoint]:
		end=midpoint
	if count>=len(numbers):
		print(f"the number {guess} does not exists")
		break

	count+=1


def binary_search(item_list,item):
	first=0
	last=len(item_list)-1

	found=False
	while (first<=last and not found):
		mid=(first+last)//2
		if item_list[mid]==item:
			found=True

		else:
			if item<item_list[mid]:
				last=mid-1

			else:
				first=mid+1


	return found

def linear_search(items,search_item):
	found=False

	start=0
	while (start<len(items) and found==False):
		if items[start]==search_item:
			found=True

		else:
			start+=1



	return found


def binary_search(items,search_item):
	start=0
	end =len(items)-1

	

	found=False


	while(found==False and start<end):
		midpoint=(start+end)//2
		if items[midpoint]==search_item:
			found=True

		else:
			if search_item>items[midpoint]:
				start=midpoint+1

			else:
				end=midpoint-1

	return found






print(binary_search(numbers,6))



	










