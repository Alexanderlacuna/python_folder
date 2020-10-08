
class MinHeap:
	# items=[0]
	def __init__(self):
		self.items=[0]


	def bubble_top(self,parentIndex,childIndex):
		if parentIndex<=0:
			return;
		else:
			print("running",self.items[parentIndex],self.items[childIndex])
			if self.items[parentIndex]>self.items[childIndex]:
				print("running inside")
				temp=self.items[childIndex]
				self.items[childIndex]=self.items[parentIndex]
				self.items[parentIndex]=temp
			return  self.bubble(parentIndex)
				# return "Success"
			

	def bubble(self,index):
		print("index  is",index)

		if index<=1:
			return "success"
		else:
			parentIndex=index//2
			# b=self.items

			rightChild=(parentIndex*2)+1
			leftChild=(parentIndex*2)
			if rightChild>len(self.items)-1:
				rightChild=None
			if leftChild>len(self.items)-1:
				leftChild=None

		if rightChild!=None and  leftChild!=None:
		
			direction=min(self.items[rightChild],self.items[leftChild])
			direction=self.items.index(direction)
			self.bubble_top(parentIndex,direction)
		elif rightChild!=None and leftChild==None:
			
			self.bubble_top(parentIndex,rightChild)
		elif rightChild==None and leftChild!=None:
			
			self.bubble_top(parentIndex,leftChild)

	def insert(self,data):
		if len(self.items)==1:
			self.items.append(data)

		else:
			self.items.append(data)
			length=len(self.items)-1
			self.bubble(length)

	def extract(self):
		if len(self.items)<=1:
			return "no item exists"
		
		else:
			target=self.items[1]
			self.items.remove(target)
			if len(self.items)==1:
				return target
			else:
				length=len(self.items)-1
				self.bubble(length)

		return target
			
			



		
class HeapNode:
	def __init__(self,data):
		self.data=data
		self.rightChild=None
		self.leftChild=None



class SingleLinkedNode:
	def __init__(self,data):
		self.data=data
		self.next=None
class SingleLinkedList:
	def __init__(self):
		self.head=None
	def insert(self,data):
		if self.head==None:
			self.head=SingleLinkedNode(data)
		else:
			current=self.head
			self.head=SingleLinkedNode(data)
			self.next=current
		return self.head




def matchingStrings(string,query):
	results=[]
	for val in query:
		results.append(string.count(val))
	return results


def lcm(a,b):
	total=1
	quit=False
	counter=2
	if a>b:
		temp=a
		a=b
		b=temp
	while (a>1 and b>1 and quit!=True):
		if (a%counter==0 and b%counter==0 ):
			total*=counter
			a=a//counter
			b=b//counter
		else:
			if counter==a:
				quit=True
			else:
				counter+=1
	if a>1:
		total*=a
	if b>1:
		total*=b
	return total

def gcd(a,b):
	if a>b:temp=b;b=a;a=temp
	counter=2
	total=1
	quit=False
	while (a>1 and b>1 and (quit==False)):
		if (a%counter==0 and b%counter==0):
			total*=counter
			a=a//counter
			b=b//counter
		else:
			if counter==a:
				quit=True
			else:

				counter+=1

	return total

def is_prime(n):
	f=True
	if j<=1:return 1
	for i in range(2,(n//2)+1):
		if n%i==0:f=False;break
	return f

def gcd_lcm(w):
	v=[]
	
	x=w-1
	k=w
	l=(x*k)
	return (x,l)

def rotate(n,d,a):
    first=list(reversed(a[0:d]))+a[d:]
    second=first[0:d]+list(reversed(first[d:]))
    fin=list(reversed(second))
    return fin

def left_rotate(n,d,a):	
	for j in range(d):
		temp=a[0]
		for i in range(1,len(a)):
			a[i-1]=a[i]
		a[-1]=temp
	return a






