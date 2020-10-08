def divide(a,b):
	try:
	  ans=a/b

	 except ZeroDivisionError:
	 	return False,None

	 else:
	 	return ans
def sort_priority(values,group):

	found=False
	def helper(x):
		nonlocal found
		if x in group:

			found=True

			

			return (0,x)
		return (1,x)

	values.sort(key=helper)

s=divide(6,2)
if s is None:
	print("invalid input")