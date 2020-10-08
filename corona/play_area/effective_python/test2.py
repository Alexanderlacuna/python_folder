class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class SLinkedList:
	def __init__(self):
		self.head=None

	def addNode(self,data):
		newNode=Node(data)

		if self.head is None:
			self.head=newNode

		else:
			current=self.head
			while(current is not None):

				current=current.next


			current.next=newNode

	def reverseNode(self):
		current=self.head

		prev=None

		while(current is not None):

			nexti=current.next



			current.next=prev
			prev=current


			current=nexti


		self.head=prev