# graphs

def gcd(a,b):
	while b:
		a,b=b,a%b
	return a
class Node(object):
	def __init__(self,name):
		self.name=name
	def getName(self):
		return self.name
	def __str__(self):
		return self.name

class Edge(object):
	def __init__(self,src,dest):
		self.src=src
		self.dest=dest
	def getSource(self):
		return self.src
	def getDestination(self):
		return self.dest
	def __str__(self):
		return self.src.getName()+"->"+self.dest.getName()

def binary(arri,target):
	low=0
	high=len(arri)-1
	while low<=high:
		# mid=(high+low)-low
		mid=low+(high-low)//2
		if arri[mid]==target:
			return mid
		else:
			if arri[mid]<target:
				low=mid+1

			else:
				high=mid-1
	return -1

def binary2(arri,target):
	print(arri)
	if len(arri)>=1:
		mid=len(arri)//2
		if arri[mid]==target:
			return mid
		else:
			print(arri)
			if arri[mid]<target:
				return  binary2(arri[mid+1:],target)
			else:
				return binary2(arri[0:mid],target)
				# go to right

	else:
		return -1
def first(arri,target,ans=-1):
	
	if len(arri)>=1:
		mid=len(arri)//2
		if arri[mid]>=target:
			ans=arri[mid]
			# do left seaarch
			return first(arri[0:mid],target,ans)
		else:

			return first(arri[mid+1:],target,ans)

	else:
		return ans

def switch(string):
	vowels=["A","E","I","O","U"]
	output=""
	back=""
	pointerA=0
	pointerB=len(string)-1
	while pointerA<pointerB:
		if string[pointerA] not in vowels:
			output+=string[pointerA]
			pointerA+=1
		if string[pointerB] not in vowels:
			back+=string[pointerB]
			pointerB-=1
		if string[pointerA] in vowels and string[pointerB] in vowels:
			output+=string[pointerB]
			back+=string[pointerA]
			pointerA+=1
			pointerB-=1
	if len(string)%2!=0:

		output+=string[pointerA]

	return (output,back)
x=[]
def recaman(n):
	# print(x)
	
	if n==0:
		x.append(0)
		return 0
	else:
		f=recaman(n-1)-n
		if f not in x and f>0:
			x.append(f)
			return f
		else:
			v=recaman(n-1)+n
			x.append(v)
			return v
def sorted_list(ari,ari2):
	combined=[]
	i=j=0
	while i<len(ari) and j<len(ari2):
		if ari[i]<ari2[j]:
			combined.append(ari[i])
			i+=1
		else:
			combined.append(ari2[j])
			j+=1
	while i<len(ari):
		combined.append(ari[i])
		i+=1
	# print(j,i)
	while j<len(ari2):
		combined.append(ari2[j])
		j+=1


	return combined

def sum_divisor(n):
	total=0
	for i in range(1,n):
		if n%i==0:
			total+=i

	return total



