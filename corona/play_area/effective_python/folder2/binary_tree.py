class Node:
	def __init__(self,data=None):
		self.data=data
		self.left_child=None
		self.right_child=None

class Binary_tree:
	def __init__(self):
		self.root=None


	def insert(self,value):
		new_node=Node(value)

		if self.root is None:
			self.root=new_node



		else:
			self._insert(value,self.root)

			

	def _insert(self,value,current_node):
		if value <current_node.data:
			if current_node.left_child is None:
				current_node.left_child=Node(value)

			else:
				self._insert(value,current_node.left_child)

		elif value>current_node.data:
			if current_node.right_child is None:
				current_node.right_child=Node(value)


			else:
				self._insert(value,current_node.right_child)

		else:
			print("node with that value already exists")


	def __repr__(self):
		if self.root:
			current_node=self.root
			while(current_node is not None):
				print(str(current_node.data))
				if current_node.left_child is not None:
					current_node=current_node.left_child

				elif current_node.left_child is not None:
					current_node=current_node.right_child

				else:
					break

				

		else:
			return "no item exists"


	def print_tree(self):
		if self.root is not None:
			self._print_tree(self.root)
			# print(nodes)


		# return values

	def _print_tree(self,current_node):

		nodes=[]
		if current_node!=None:
			self._print_tree(current_node.left_child)
			print(str(current_node.data))
			nodes.append(str(current_node.data))

			self._print_tree(current_node.right_child)
		

		return nodes

	def height(self):
		if self.root is not None:
			return self._height(self.root,0)
		return 0

	def _height(self,cur_node,cur_height):
		if cur_node is None:
			return cur_height
		right_height=self._height(cur_node.right_child,cur_height+1)

		left_height=self._height(cur_node.left_child,cur_height+1)
		return max(right_height,left_height)


	def  search_node(self,value):
		if self.root is None:
			return "no node exists"

		else:
			return self._search_node(self.root,value)

	def _search_node(self,current_node,value):
		if current_node is None:
			return "not  found"

		else:
			if value>current_node.data:
				return self._search_node(current_node.right_child,value)

			elif value<current_node.data:
				return self._search_node(current_node.left_child,value)

			else:
				return "found"







# create an empty tree

tree=Binary_tree()
tree.insert(4)
tree.insert(8)
tree.insert(3)
tree.insert(1)
# tree.insert(8)
print(tree.search_node(8))
print(tree.search_node(18))
print(tree.print_tree())
print(tree.height())

# LET make a binary tree
class Node:
	def __init__(self,value):
		self.data=value
		self.left_child=None
		self.right_child=None

class BinaryTree:
	def __init__(self):
		self.root=None

	def insert(self,value):
		if self.root is None:
			self.root=Node(value)

		else:
			self._insert(self.root,value)


	def _insert(current_node,value):
		if current_node.data==value:
			print("node  already exists")

		else:
			if current_node.data >value:
				if current_node.left_child is None:
					current_node.left_child=Node(value)

				else:
					self._insert(current_node.left_child,value)

			if current_node.data<value:

				if current_node.right_child is None:
					current_node.right_child=Node(value)

				else:
					self._insert(current.right_child,value)


	def height(self):
		if self.root is None:
			return "no node exists"

		else:
			return self._height(self,current_height,current_height=0)


	def _height(self,current_node,current_height):
		if  current_node is None:
			return current_height

		else:
			right_height=self._height(current_node.right_child,current_height+1)

			left_child=self._height(current_node.left_child,current_height+1)

			return max(right_child,left_child)


	def search_node(self,value):
		if self.root is None:
			return "binary tree does not have node"

		else:
			return self._search_node(self.root,value)

	def _search_node(self,current_node,value):

		found=False
		if self.current_node is None:
			return found

		else:
			if current.node.data>value:

				# go to the leftsel
				self._search_node(current_node.left_child,value)

			elif current_node.data<value:
				self._search_node(current_node.right_child,value)

			else:
				found=True

		return found




class Node:
	def  __init__(self,data):
		self.data=data
		self.previos=None

		self.next=None



class DlinkedList:
	def __init__(self):
		self.head=None

		self.tail=None

	def insert(self,value):
		if self.head is None:
			self.head=Node(value)

		else:
			self._insert(self.head.next,value)


	def _insert(self,curent_node,value):
		if current_node.next is  None:
			new_node=Node(value)

			current_node.next=Node(value)
			new_node.previos=current_node
			# curent_node.next=Nonene

		else:
			self._insert(current_node.next,value)

	def print_node(self):
		nodes=[]
		current_node=self.head

		while (current_node is not  None):
			nodes.append(current_node.data)

		nodes.append("None")

		return "->".join(nodes)




s=DlinkedList()











