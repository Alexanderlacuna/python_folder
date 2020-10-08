class LinkedList:
	def __init__(self):
		self.head=None



class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

	def __repr__(self):
		return self.data


class LinkedList:
	def __init__(self):
		self.head=None

	def __repr__(self):
		node=self.head
		nodes=[]
		while node is not None:
			nodes.append(node.data)
			node=node.next

		nodes.append("None")

		return "->".join(nodes)

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

	def __repr__(self):
		return f'{self.data}'

# linked list needs only the head

class LinkedList:
	def __init__(self):
		self.head=None
	def __repr__(self):

		node=self.head
		nodes=[]

		while node is not None:
			nodes.append(node.data)
			node=node.next

		nodes.append("None")

		return "->".join(nodes)




	def deque(self):
		self.head=self.head.next


	def addtoIndex(self,item,value):
		targetNode=None

		updated=False
		current=self.head

		while(current.data!=item and current is not None):
			# targetNode=current
			# current=current.next
			targetNode=current.next
			current=current.next


		if targetNode is not None:
			newNode=Node(value)
			currentNext=targetNode.next
			targetNode.next=newNode
			targetNode.next.next=currentNext







	def at_the_beginning(self,new_Data):
		new_node=Node(new_Data)

		new_node.next=self.head
		self.head=new_node

	def at_the_end(self,new_Data):
		new_node=Node(new_Data)

		if self.head==None:
			self.head=new_Data

		else:
			lastval=self.head

			while(lastval.next):
				lastval=lastval.next
			lastval.next=new_node

	def remove_at_end(self):

		if self.head==None:
			return "No item in the list"
		lastval=self.head
		while(lastval.next):
			lastval=lastval.next


		current_node=self.head

		target_node=None

		while(current_node):
			if current_node.next==lastval:
				target=current_node


				target.next=None




			current_node=current_node.next

		return (current_node,lastval)


	def reverselinked(self):
		prev=None
		current=self.head
		while(current is not None):
			nexti=current.next

			current.next=prev

			prev=current
			current=nexti

		self.head=prev


	def reverselinked(self):
		prev=None
		current=self.head
		while(current is not None):
			nexti=current.next
			current.next=prev
			prev=current
			current=nexti

		self.head=prev

	def reverselinked(self):
		current=self.head
		prev=None
		while(current is not None):
			nexti=current.next
			current.next=prev
			prev=current
			current=nexti

		self.head=prev


	def reverselinked(self):
		prev=None
		current=self.head

		while(current is not None):

			nexti=current.next
			current.next=prev
			prev=current
			current=nexti

		self.head=prev




	





class DoubleNode:
	def __init__(self,data):
		self.data=data
		self.previosNode=None
		self.nextNode=None


	def __repr__(self):

		if  self.previosNode==None:
			return f'{self.data}->{self.nextNode}'



		


		return f'{self.data}'






class DoubleLinked:
	def __init__(self):
		self.head=None


	def __repr__(self):
		nodes=[]

		node=self.head

		while(node is not None):
			nodes.append(node.data)
			node=node.nextNode

		nodes.append("None")
		return "->".join(nodes)


	def addNode(self,newData):
		new_node=DoubleNode(newData)

		if self.head is None:
			self.head=new_node


		else:
			last_node=self.head
			while(last_node.nextNode):
				last_node=last_node.nextNode

			last_node.nextNode=new_node
			new_node.previosNode=last_node

	def removeHead(self):
		next_to_head=self.head.next
		next_to_head.previosNode=None

		self.head=next_to_head


	def doublereverse(self):

		"""
		aim
		"""
		prev=None
		# nexti=
		current=self.head

		while(current is not None):
			nexti=current.nextNode
			current.nextNode=prev
			prev=current


			current=nexti

		self.head=prev


	def doublelinkedreverse(self):
		prev=None
		current=self.head
		while(current is not None):
			nexti=current.nextNode
			current.nextNode=prev
			current.previosNode=nexti
			prev=current
			current=nexti


		self.head=prev


	def doublelinkedreverse(self):
		prev=None
		current=self.head
		# nextGen=None

		while(current is not None):

			nexti=current.nextNode
			previ=current.previosNode


			current.nextNode=prev
			current.previosNode=nexti



			prev=current

			current=nexti
			# next_to=current.nextNode
			# prev_to=current.previosNode
			# current.nextNode=prev
			# current.previosNode=next_to

			# prev=current

		    



			# current=next_to


		self.head=prev

	# def doublelinkedreverse(self):
	# 	prev=None
	# 	current=self.head
	# 	while(current is not None):
	# 		nexti=current.nextNode
	# 		current.nextNode=prev
	# 		prev=current
	# 		current=nexti

	# 	self.head=prev


	def reverseLinked(self):
		# get the last node to be the head 
		last_node=self.head

		while(last_node.nextNode):
			print(last_node)
			last_node=last_node.nextNode


		print(f"the last node is {last_node}")

		new_node=last_node
		# self.head=new_node
		# print(last_node)

		while(new_node.previosNode is not None):

			previos=new_node.previosNode
			nexa=new_node.nextNode



			new_node.nextNode=new_node.previosNode
			new_node.previosNode=previos
			new_node=previos

			# new_node=new_node.nextNode


				# 	print(f"previos node is {new_node.previosNode}")

		# 	print(last_node.previosNode)


		# 	
		# 	
		# 	new_node=new_node.previosNode


		# self.head=new_node





		# get the previos node






	#
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.previos=None


	def __str__(self):
		return self.data


class Circular:
	def __init__(self):
		self.head=None
		self.tail=None

	def addNode(self,data):

		newNode=Node(data)
		print(newNode)
		if self.head is None:
			self.head=newNode
			self.tail=self.head

		else:
			current=self.head
			while(current.next is not self.head):
				current=current.next
			current.next=newNode
			newNode.previos=current
			self.tail=newNode
			# newNode.next=self.head

		self.tail.next=self.head





	def __repr__(self):
		# print("running code")
		# return "hello
		nodes=[]
		node=self.head
		while(node is not self.tail):
			nodes.append(node.data)
			node=node.next

		nodes.append(node.data)

		return '->'.join(nodes)










llist=LinkedList()


first_node=Node("A")
second_node=Node("B")
llist.head=first_node

first_node.next=second_node

second_node.next=Node("C")
# llist.deque()
llist.at_the_beginning("F")

llist.at_the_end("W")
print(llist)
# print(llist.remove_at_end())
print(llist)

print(llist.reverselinked())

print(f" testing {llist.addtoIndex('F','K')}")
# llist.addtoIndex("W","ER")
print(llist)


dblist=DoubleLinked()

first_node=DoubleNode("A")
dblist.head=first_node
dblist.addNode("B")
print(dblist)
dblist.doublelinkedreverse()
# print(first_node)
print(f'the double list {dblist.head.nextNode.previosNode}')
# print(dblist.head.nextNode.previosNode.data)


clist=Circular()
clist.addNode("U")
clist.addNode("T")
clist.addNode("O")
clist.addNode("I")
clist.addNode("Y")

print(clist)
print(clist.tail)

class Node:
	def __init__(self,data):
		self.data=data
		self.previos=None
		self.next=None

	def __repr__(self):
		return self.data

class Circular:
	def __init__(self):
		self.head=None
		self.tail=None

	def addNode(self,data):
		newNode=Node(data)
		if self.head is None:
			self.head=newNode
			self.tail=self.head

		else:
			# current_tail=self.tail
			current=self.tail
			current.next=newNode
			newNode.previos=current
			newNode.next=self.head
		self.tail=newNode


	def __repr__(self):
		nodes=[]
		current=self.head
		if(current is None):
			return "none item exists"

		while(current is not self.tail):
			nodes.append(current.data)
			current=current.next


		nodes.append(current.data)
		return "->".join(nodes)
	


nclist=Circular()
nclist.addNode("A")
nclist.addNode("B")
nclist.addNode("C")
print(nclist.tail)
print(nclist.tail.next)




# print(clist.tail.previos)


# print(clist.tail)
# print(clist.tail.previos)
# print(clist.tail.next)

# print(clist.head.next)
# print(first_node.nextNode)
# print(dblist.head.nextNode.previosNode)
class DoubleList:
	def __init__(self):
		self.head=None
	def addNode(self):
		current=self.head
		prev=None


		while (current is not None):
			nexti=current.next

			current_prev=current.prev
			current.next=prev
			current.prev=nexti

			prev=current




			current=nexti

		current=prev

	def __repr__(self):
		nodes=[]
		node=self.head
		
		
		while(node is not None):
			nodes.append(node.data)
			node=node.next

		nodes.append("None")

		return "->".join(nodes)






