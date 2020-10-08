array=[1,4,5,4,3,2,7,9,5,4]
new_array=sorted(array)
dicti={}
for item in array:
	if  item not in dicti:
		dicti[item]=1

	else:
		dicti[item]+=1

# print(dicti)
sorted_array=[]

"""
while provided the dictionary is empty


"""
# print(dicti)

# print(f' the dicito {dicti.items()}')
d=sorted(dicti.items(),key=lambda item:item[1])
array=[]
for key,value in d:
	while value>0:
		array.append(key)
		value-=1
	# while value>0:
	# 	array.append(key)
	# array.append(f'{key}  '*value)



# d=sorted(dicti.values(),)
# print(d)
# print(f"the sorted is {d}")

print(array)
# while len(dicti)>1:

# 	maximum_items=0
# 	for key in dicti.keys():
# 		print(key)

		# dict[key]=None


	# pass


class Duplicates:

	dicti={}

	duplicated_array=[]
	def __init__(self,array):
		self.array=sorted(array)


	def  setDicti(self):

		for item in self.array:
			if item not in self.dicti:
				self.dicti[item]=1

			else:
				self.dicti[item]+=1

	def sort_dicti(self):
		return sorted(self.dicti.items(),key=lambda item:item[1])


	def get_results(self):

		# print(f'{self.dicti}')

		for key,value in  self.sort_dicti():
			while value>0:
				self.duplicated_array.append(key)

				value-=1



	def __len__(self):
		return len(self.duplicated_array)

	def final_results(self):
		# if self.duplicated_array>0:

		if  len(self.duplicated_array)>0:

			return self.duplicated_array


	def get_direct_duplicates(self):
		self.setDicti()
		self.sort_dicti()
		self.get_results()
		return self.final_results()


s=Duplicates([1,4,4,4,5,4,2,2,1,33,3,3,3,32,3])

# print(s.get_direct_duplicates())
d=s.get_direct_duplicates()
print(d)




# print( f"value s are {q}")
# print(s.sort_dicti().get_results().final_results())
# print()


		# get_dicti=self
		



	# def __str__


# binary sort,is find mid divide into tow
def find_mid(array):

	# sorted()

	start=array[0]
	end=len[array]

	fn_sort(start,end)

def compute_factorial(num):

	if num<1:
		return 1
	else:
		return num*compute_factorial(num-1)

print(compute_factorial(5))
