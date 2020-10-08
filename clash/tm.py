class Node:
	def __init__(self,data):
		self.data=data
		self.next=None


class LinkedList:
	def __init__(self):
		self.head=None
	def insert(self,data):
		if self.head != None:
			curr=self.head
			while curr.next!=None:
				curr=curr.next

			curr.next=Node(data)

		
		else:
			self.head=Node(data)

		return self.head
	def println(self):
		t=[]
		curr=self.head
		while curr:
			t.append(curr.data)
			curr=curr.next

		return t

	def deletion(self,val):
		curr=self.head
		if curr is None:
			return False

		elif curr.next is None:
			self.head=None

			return True
		else:
			prev=None
		
			while curr!=None:
				

				if curr.data==val:
					prev.next=curr.next
					break
					
				else:
				
					prev=curr
					curr=curr.next


		return True
class Nodes:
	def __init__(self,data):
		self.data=data
		self.leftChild=None
		self.rightChild=None


class Binary:
	def __init__(self):
		self.root=None
	def insert(self,val):
		if self.root is None:
			self.root=Nodes(val)
		else:
			self._insert(self.root,val)

	def _insert(self,node,val):
		# curr=self.root

		if node.leftChild==None and node.data>val:
			node.leftChild=Nodes(val)
		elif node.rightChild==None and node.data<val:
			node.rightChild=Nodes(val)
		else:

			if val>node.data:
				self._insert(node.rightChild,val)

			else:
				self._insert(node.leftChild,val)

		return True

	def gets(self):
		v=self.query(self.root)
		return v

	def query(self,curr,store=[]):

		if curr==None:
			return False

		# store=[]

		if len(store)==0:
			store.append(curr.data)
		
		# store.append(curr.data)
		if curr.leftChild:
			store.append(curr.leftChild.data)
			self.query(curr.leftChild,store)
		if curr.rightChild:
			store.append(curr.rightChild.data)
			self.query(curr.rightChild,store)

		return store

		# else:

		# print(store)



					
					
					
				

		


