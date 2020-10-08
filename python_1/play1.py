# trying on recursion

import time
def computeSum(n):

	
	if n!=0:
		print(n*"[]")
		n=n-1
		computeSum(n)


# computeSum(20)
def factorial1(n):
	if(n==0 or n==1):
		return 1

	else:
		return  n*factorial1(n-1)

# fib
def fibonacci(n):
	if n==1 or n==2:
		return 1
	elif n>2:
		return fibonacci(n-1)+fibonacci(n-2)


# print(factorial(3))
# for i in range(1,200):
# 	print(fibonacci(i))
fibonacci_cache={}
def fibonacci2(n):
	if  n in fibonacci_cache:
		return fibonacci_cache[n]
	if n==1 or n==2:
		return 1

	elif n>2:
		value=fibonacci(n-1)+fibonacci(n-2)
		fibonacci_cache[n]=value
		return value


f=time.time()

for i in range(1,10):
	print(fibonacci(i))

print("finished")
for i in range(1,10):
	print(fibonacci2(i))


# print("the time" + " " +time.time()-f)
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
	if n==1 or n==2:
		return 1
	else:
		return fibonacci(n-1)+fibonacci(n-2)

cached={}
def factorial(n):

	if n in cached:
		return cached[n]


	if n==0 or n==1:
		return 1
	else:
		value=n*factorial(n-1)
		cached[n]=value
		return value

x=time.time()
# print(factorial(500))
c=time.time()-x
# print(c)
r=time.time()
# print(factorial1(500))
f=time.time()-r
# print(f-c)


# tower of hanoi
def hanoi(n,source,helper,target):
	if n>0:
		# move tower of size n-1 to helper
		hanoi(n-1,source,target,helper)

		if source:
			target.append(source.pop())

		hanoi(n-1,helper,source,target)


source=[4,3,2,1]
target=[]
helper=[]
hanoi(len(source),source,helper,target)

def largestRange(array):
	newAri=sorted(array)
	largest=[]
	currentLargest=[]
	pointer=0

	while len(currentLargest)<len(newAri):
		if newAri[pointer+1]==newAri[pointer]+1:
			currentLargest.append(newAri[pointer])
			pointer+=1

		else:
			currentLargest.append(newAri[pointer])
			if len(largest)<len(currentLargest):
				largest=currentLargest
			currentLargest=[]
			# pointer+=1
			continue
			currentLargest=[]


	return largest

def largestRange(array):
	counter={}
	left=0
	right=0
	pointer=0
	for i in range(0,len(array)):
		counter[array[i]]=0

	for i in range(0,len(array)):
		if array[i]-1 in counter:
			left=array[i]-1
		if array[i]+1 in counter:
			right=array[i]+1

	return counter



def duplicate(array):
	counter={}
	for num in array:
		if num in counter:
			counter[num]+=1

		else:
			counter[num]=1
	# counter={x:0 for x in array}
	for key in counter:
		if counter[key]>1:
			counter[key]=False

	# return [num for num in counter  if  counter[num]>1]
	return counter




		
# print(source,helper,target)

# print(largestRange([12,11,10,9,7,2,3,4,5,1,6,40,41,42,43,44,45,46,47,48,49,50,51,52,53]))

print(duplicate([12,12,3,11,10]))

