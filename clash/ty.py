def insertion(arri):
	pointer=1

	current_index=pointer
	starter=0

	while current_index<len(arri)-1:

		while arri[starter]>arri[pointer]:
			swap(arri,starter,pointer)


		# if arri[starter]>arri[pointer]:
			


def  swap(arri,index1,index2):
	temp=arri[index1]
	arri[index1]=arri[index2]
	arri[index2]=temp
def selection(arri):
	f=[]
	counter=len(arri)
	pointer=0


	while pointer!=counter:
		g=select(arri[pointer:],pointer)
		
		temp=arri[pointer]

		arri[pointer]=arri[g]
		arri[g]=temp
		pointer+=1
		
	

	return arri

def select(arri,start):
	smallest=None
	index=0

	for i,val in enumerate(arri,start):
		if smallest==None:
			smallest=val
			index=i
		else:
			if smallest>val:
				smallest=val
				index=i
	return index
def insert(arri):
	pointer=0
	curr=1

	while curr<len(arri):

		if arri[pointer]>arri[curr]:
			print("yes performing tasks")
			current_shadow=curr
			pointer_shadow=pointer
			while arri[pointer_shadow]>arri[current_shadow] and pointer_shadow>=0:
				print("yes performing task")

				# prev=pointer_shadow
				temp=arri[pointer_shadow]
				arri[pointer_shadow]=arri[current_shadow]
				arri[current_shadow]=temp
				current_shadow-=1
				pointer_shadow-=1


		pointer+=1
		curr+=1

	return arri




def merge(arri):
	if len(arri)>1:
		mid=len(arri)//2
		leftHand=arri[:mid]
		rightHand=arri[mid:]
		merge(leftHand)
		merge(rightHand)

    # i=j=k=0
    while len(leftHand)>i and len(rightHand)>j:
    	if leftHand[i]>rightHand[j]:
    		arri[k]=leftHand[i]
    		i+=1
    		k+=1



    	else:
    		arri[k]=rightHand[j]:
    		j+=1
    		k+=1

    while len(leftHand)>i:
    	arri[k]=leftHand[i]
    	i+=1
    	k+=1

    while len(rightHand)>j:
    	arri[k]=rightHand[j]
    	j+=1
    	k+=1

    return arri

   class MaxHeap:
   	items=[None]
   	def insert(val):
   		if len(items)==1:
   			items[1]=val
   		else:
   			items.append(val)
   			indexlast=len(items)-1

   			treeShake(indexlast)

   	def treeShake(node):
   		
   		if   node==1:
   			return
   		else:
   			parent=indexlast//2
   			leftChild=(indexlast*2)
   			rightChild=(indexlast*2)+1
   			while parent<leftChild or parent<rightChild:
   				temp=parent
   				if leftChild>rightChild:
   					leftChild=parent
   					parent=temp
   					
   				else:
   					rightChild=parent
   					parent=temp

   		    treeShake(parent)
   				

   				
