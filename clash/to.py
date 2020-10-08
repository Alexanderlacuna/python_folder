
#g=[43,32,11,78,90,45,111,7,28]


def quickSort(arri,pivot=0):
	print(arri)
	print("the pivot is",pivot)

	i=1
	j=len(arri)-1

	while i<j:
		print("the values of i and j are",i,j)

		if arri[i]>arri[pivot]:
			print("yea i got a value to change",arri[i])
			if arri[j]<arri[pivot]:
				print("best thing to happen")
				temp=arri[i]
				arri[i]=arri[j]
				arri[j]=temp
				i+=1
				j-=1
			else:
				print("bad luck j")
				j-=1
		else:
			print("bad luck i")
			i+=1
	
			
		

	pivot=i-1

	for i in range(1,len(arri)):
		if arri[i]>arri[i-1]:
			pass
		else:
			return quickSort(arri,pivot)

	

	
	# return quickSort(arri)


class MinHeap:
	def __init__(self):
		self.items=[0]

	def insert(self,val):
		if len(self.items)==1:
			self.items.append(val)
		else:
			self.items.append(val)
			index=len(self.items)-1
			return self.minShakeUp(index)

	def helper(self,parentIndex,childIndex):
		print("running helper function")
		if parentIndex>0:
			# do to the job
			temp=self.items[parentIndex]
			if self.items[parentIndex]>self.items[childIndex]:
				print("yes our parentisBigger",self.items[parentIndex],self.items[childIndex])
				self.items[parentIndex]=self.items[childIndex]
				self.items[childIndex]=temp
				self.minShakeUp(parentIndex)
			    # self.minShakeUp(parentIndex)





	def minShakeUp(self,index):
		print("index is",index)
		if index<=1:
			return "finished"

		else:
			parent=index//2
			leftChild=parent*2
			rightChild=(parent*2)+1
			print("parent is and left and right",parent,leftChild,rightChild)
			noItems=len(self.items)-1
			if leftChild>noItems:
				leftChild=None
			if rightChild>noItems:
				rightChild=None

			if leftChild!=None and rightChild!=None:
				print("both exists",leftChild,rightChild)
				if self.items[leftChild]<self.items[rightChild]:
					print("yes going to left")
					self.helper(parent,leftChild)
				else:
					print("yes going to right")
					self.helper(parent,rightChild)
					# go to right
				# good thing
			elif leftChild!=None and rightChild==None:
				print("only left exists")
				self.helper(parent,leftChild)
			elif rightChild!=None and leftChild==None:
				print("only right exists")
				self.helper(parent,rightChild)




class Max2Heap:
	def __init__(self):
		self.items=[0]
	def insert(self,val):
		if len(self.items)==1:
			self.items.append(val)

		else:
			self.items.append(val)
			print(len(self.items))
			index=len(self.items)-1
			return self.shakeHeap(index)

	def extract(self):
		if len(self.items)>1:
			return  self.items[1]
		return "No item exists"

	def moveToSide(self,index,parentIndex):
		if parentIndex>0:

			temp=self.items[parentIndex]
			if self.items[index]>self.items[parentIndex]:
				self.items[parentIndex]=self.items[index]
				self.items[index]=temp

				self.shakeHeap(parentIndex)

	def delete(self):

		if len(self.items)==1:
			return "No item"


		deleting=self.items[1]

		
		
		if len(self.items)>2:
			self.items[1]=self.items[len(self.items)-1]
			temp=self.items[len(self.items)-1]
			self.items.remove(temp)
			self.shakeHeap(len(self.items)-1)

		else:
			self.items.remove(self.items[1])

		return deleting
			

			# shakeup


	def shakeHeap(self,index):
		print("the index is ",index)

		if index<=0:
			return "Finished"
		else:

			try:
				parent=index//2
				leftChild=parent*2
				rightChild=(parent*2)+1
				if leftChild>len(self.items)-1:
					print("leftChilsd yes")
					leftChild=None
				if rightChild>len(self.items)-1:
					print("rightChild yes")
					rightChild=None
				
				if leftChild!=None and rightChild!=None:
					print("am going to both left and right")
					print("the leftChild and the rightChild is",leftChild,rightChild)
					if self.items[leftChild]>self.items[rightChild]:
						self.moveToSide(leftChild,parent)
						# self.shakeHeap(leftChild)
					
					else:
						self.moveToSide(rightChild,parent)
						# self.shakeHeap(rightChild)
						



				elif leftChild!=None and rightChild==None:
					print("am only goinh to left")
					self.moveToSide(leftChild,parent)
					# self.shakeHeap(leftChild)

				elif leftChild==None and rightChild!=None:
					print("am only going to right")
					self.moveToSide(rightChild,parent)
					# self.shakeHeap(rightChild)
					# go to right
			except IndexError as e:
				print("the index error is ",str(e))
				return "1"


class MaxHeap:
	items=[0]
	def insert(self,val):
		if len(self.items)==1:
			self.items.append(val)
		else:
			self.items.append(val)
			lastItem=len(self.items)-1
			return self.treeShake(1)

	def showHeap(self):
		return self.items

	def delete(self):
		parent=self.items[1]
		if len(self.items)==1:
			self.items.remove(parent)
		else:
			last=self.items[-1]
			self.items.remove(self.items[-1])
			self.items[1]=last

			self.treeShake(1)

		return parent
			# self.items.delete()\\

	def extract(self):
		return self.items[0]

	def treeShake(self,node):

		print(node)
		leftChild=node*2
		rightChild=(node*2)+1
		parent=node

		try:
			temp=self.items[parent]
			if self.items[leftChild]>self.items[rightChild]:
				print("working on left")
				if self.items[leftChild]>self.items[parent]:
					print("yes i will change left")
					
					self.items[parent]=self.items[leftChild]
					self.items[leftChild]=temp

			elif self.items[rightChild]>self.items[leftChild]:
				print("working on right")
				if self.items[rightChild]>self.items[parent]:
					print("yes i will actually change right")
					
					self.items[parent]=self.items[rightChild]
					self.items[rightChild]=temp


			self.treeShake(leftChild)
			self.treeShake(rightChild)

			# treeShake(leftChild)
		 #    treeShake(rightChild)




		except IndexError as e:
			return "fin"

		# treeShake(leftChild)
		# treeShake(rightChild)

		



