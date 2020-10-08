# functions using specific error instead of error

def  divide(a,b):

	if isinstance(a&b,int):
		


		try:
			return True ,a/b

		except ZeroDivisionError:
			return False,None

	else:
		return "the input is invalid"

	# else:
	# 	return "unsupported error"

	# return "invalid input"


# print(divide(3,2)) 
# print(divide(3,0))
# print(divide("SDsd",3))
# print(divide(3,"WDadaw"))

def sort_priority(value,group):

	found=False
	def helper(x):
		if x in group:
			found=True
			return (0,x)
		
		return (1,x)
	value.sort(key=helper)

	return found

numbers=[1,2,3,4,5,3,1,2,76]
group={12,22,31,2,3,5}
# print(sort_priority(numbers,group))
def sortingKey(x,y):
	return x-y
	# return val[0]-val[1]


	
	

	

s=[2,1,5,6,8,5,1,20]
# print(s.sort(key=sortingKey))
# sort by key key is called everytime
student_tuples=[
('jane',15),
('dane',12),
('jude',10)


]
s=sorted(student_tuples,key=lambda student:student[1])
print(s)

from operator import itemgetter,attrgetter
print(sorted(student_tuples,key=itemgetter(0)))


class BySubjectGrade(object):
	def __init__(self):
		self._grades={}
	def addStudent(self,name):
		self._grades[name]=1


		