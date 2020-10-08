
class MaxHeap:

	items=[None]
	def insert(val):
		if len(items)==1:
			items[1]=val
		else:
			items.append(val)
			indexlast=len(items)-1

		return treeShake(indexlast)


   def tree:
      pass
   # def tree:
   #    pass
   # def treeShake(node):
   #    if node==1:
   #       return 

   #    else:
   #       parent=node//2
   #       leftChild=node*2
   #       rightChild=(node*2)+1
   #       if parent<leftChild or parent<rightChild:
   #          temp=parent
   #          if leftChild>rightChild:
   #             leftChild=parent
   #             parent=temp
   #          else:
   #             rightChild=parent
   #             parent=temp
   #       treeShake(parent)




	# def treeShake(node):
		
	# 	if   node==1:
	# 		return
	# 	else:
	# 		parent=indexlast//2
	# 		leftChild=(indexlast*2)
	# 		rightChild=(indexlast*2)+1
	# 		while parent<leftChild or parent<rightChild:
	# 			temp=parent
	# 			if leftChild>rightChild:
	# 				leftChild=parent
	# 				parent=temp
					
	# 			else:
	# 				rightChild=parent
	# 				parent=temp

 #      treeShake(parent)

		   # treeShake(parent)
				