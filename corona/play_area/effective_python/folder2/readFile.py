with open("./file.txt",'r') as text:
	s=text.readline()
	# data

	target=[word for word in s.split() if len(word)>9]

	# print(target)

def readfile(filepath):
	with open(filepath,"r") as text:
		data=text.readline()


	return data



def word_exists(targetword):

	data=readfile("./file.txt")
	data_array=data.split()
	# print(data_array)

	ans=binary_search(data_array,"dolor")



	return ans





def binary_search(words_array,target):


	words=sorted(words_array)

	if isinstance(words[0],str):
		words=sorted(words,key=lambda d:len(d))
	# print(words)
	# print(words)

	start=0
	end=len(words)-1
	# print(f'the length of words is {end}')
	
	mid=0
	found=False
	# print(words)

	while(start<=end):

		mid=((start+end)//2)
		# print(mid)
		if words[mid]==target:
			print("worked")

			# print(f'running the required function us here')
			found=True


			break

		else:
			if  target>words[mid]:
				start=mid+1
			else:
				end=mid-1


	return found






s=word_exists("voluptas")
i=word_exists('delectus')
f=word_exists('incidunt')
q=word_exists('incisaq')
print(s,i,f,q)

s=[1,2,3,4,5,19]
a=binary_search(s,2)
print(a)
# voluptas', 'delectus', 'incidunt',
	# words=text.split(" ")
	


	# print(words)
	# print(value)	
UNDEFINED=object()
def divide_json(path):
	handle=open(path,"r+") #may rise ioerror
	try:

		data=handle.read()
		op=json.load(data) #may raise value error
		value=(op["numerator"]/op['denominator']) #may raise  zero division error


	except ZeroDivisionError as e:
		return UNDEFINED


	else:
		op['result']=value
		result=json.dumps(op)
		handle.seek(0)
		handle.write(result) #may raise  IOerror
		return value

	finally:
		handle.close()


# consider returning iterators rather than a list

def index_words(text):
	result=[]
	if text:
		result.append(0)

	for index,letter in enumerate(text):
		if letter==" ":
			result.append(index+1)

	return result 


# tryind to use iterate

def index_words(text):
	if text:
		yield 0

	for index,letter  in enumerate(text):
		if letter==" ":
			yield index+1



w=list(index_words("Wdwefwe efwfew ewffe"))
def index_file(handle):
	offset=0
	for line in handle:
		if line:
			yield offset

		for letter in line:
			offset+=1
			if letter== ' ':
				yield  offset



