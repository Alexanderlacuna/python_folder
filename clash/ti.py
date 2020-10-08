def pick_finder(ari):
	# print(ari)
	if len(ari)>1:
		mid=len(ari)//2
		if ari[mid-1]>ari[mid]:
			return pick_finder(ari[0:mid])
		elif ari[mid+1]>ari[mid]:
			return pick_finder(ari[mid+1:])
			# go to right

		else:
			return ari[mid]
	else:
		return ari[0]

def dimensional_finder(matrix):
	print(matrix)
	col=len(matrix)//2 
	print("the col is ",col)
	 #this is our j
	start=None
	index=None

	# i=matrix[j].index(max(matrix[j]))

	_max=None

	if col==1:

		for row in range(len(matrix)):
			if row==0:
				_max=matrix[row][0]
			else:
				_max=max(_max,matrix[row][0])

		return _max


	
		
		




	for row in matrix:
		if start==None:
			start=row[col]
			index=row.index(start)
		elif row[col]>index:
			start=row[col]
			index=row.index(start)

	row=index

	if matrix[row][col]<matrix[row][col-1]:

		f=[row[:col] for row in matrix]
		return dimensional_finder(f)
		# go to left
	elif matrix[row][col]<matrix[row][col+1]:
		f=[row[col+1:] for row in matrix]
		return dimensional_finder(f)
		# go to right
	else:
		return matrix[row][col]





def matrix(row_column_matrix):
	for i in range(4):
		length=4-i
		temp=row_column_matrix[i][0]
		for j in range(4):
			row_column_matrix[i][j]=row_column_matrix[length-j][i]
			# row_column_matrix[i][j+1]=row_column_matrix[2][i]
			# row_column_matrix[i][j+2]=row_column_matrix[1][i]
		new_temp=row_column_matrix[i][j+3]
		row_column_matrix[i][j+3]=temp
		temp=new_temp

	return row_column_matrix

def transpose(matrix):
	for row in range(len(matrix)):
		for c in range(row,len(matrix[0])):
			temp=matrix[c][row]
			matrix[c][row]=matrix[row][c]
			matrix[row][c]=temp

	# swap
	for i in  range(len(matrix)):
		start=0
		end=len(matrix)-1
		while (start<end):	
			temp=matrix[i][end]
			matrix[i][end]=matrix[i][start]
			matrix[i][start]=temp
			start+=1
			end-=1



	return matrix


def hasSum(arri,target):
	low=0
	high=len(arri)-1
	while (low<high):
		if arri[low]+arri[high]==target:
			return True

		elif arri[low]+arri[high]>target:
			high-=1
		elif arri[low]+arri[high]<target:
			low+=1

	return False
def optimalSum(arri,target):
	f=set()
	for val in arri:
		diff=target-arri
		if diff in f:
			return True
		else:
			f.add(val)

	return False


class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class SingleLinkedList:
	def __init__(self):
		self.head=None
	def insert(self,data):
		if self.head==None:
			self.head=Node(data)
		else:
			current=self.head
			while (current.next!=None):
				current=current.next
			current.next=Node(data)

	def printLinked(self):
		temp=[]
		if self.head==None:
			return "empty"
		else:
			current=self.head
			while (current!=None):
				temp.append(str(current.data))
				current=current.next

			temp.append("None")
		return "->".join(temp)

	def reverse(self):
		prev=None
		curr=self.head
		while (curr.next!=None):
			# print("the previous is ",prev)
			

			nexti=curr.next

			curr.next=prev
			prev=curr
			curr=nexti

		curr.next=prev
		self.head=curr

		return self.printLinked()
		



class DNode:
	def __init__(self,data):
		self.data=data
		self.prev=None
		self.next=None

class DoubleLinkedList:
	def __init__(self):
		self.head=None

	def insert(self,data):
		if self.head==None:
			self.head=DNode(data)
		else:
			curr=self.head
			prev=None
			while (curr.next!=None):
				curr=curr.next
			curr.next=DNode(data)
			curr.next.prev=curr

	def printDouble(self):
		if self.head==None:
			return "Empty "
		else:
			temp=[]
			curr=self.head
			while(curr!=None):
				temp.append(str(curr.data))
				curr=curr.next
			temp.append("None")
			return "->".join(temp)

	def reverse(self):
		prev=None

		curr=self.head

		while(curr.next!=None):
			nexti=curr.next
			curr.prev=curr.next
			curr.next=prev
			prev=curr

			curr=nexti

		curr.next=prev
		self.head=curr

		return self.printDouble()


