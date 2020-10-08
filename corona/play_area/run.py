class Arithmetic(Exception):

	def __init__(self):
		msg="this is a test"
		super().__init__(msg)

class DuplicateKeyError(Exception):
	def __init__(self,duplicate_key):
		msg=f'Item with key {duplicate_key} exists'



class  SimpleGradeBook(object):
	_grades={}

	def addStudent(self,name):


		if name in self._grades.keys():

			newStudent.addStudent(name="alex")

			

		self._grades[name]=[]


		
		
	def report_grade(self,name,score):



		try:
			self._grades[name].append(score)


		except KeyError:
			raise Arithmetic()




		
	# def __len__(self,item):
	# 	return  len(item)

	def  average_grade(self,name):
		try:
			grades=self._grades[name]


		except TypeError:
			raise Arithmetic()

		# else:
		# 	raise Arithmetic()

		return sum(grades)/len(grades)


newStudent=SimpleGradeBook()
print(newStudent)
newStudent.addStudent(name="alex")

newStudent.report_grade(name="alex",score=43)
d=newStudent.average_grade("alex")
# newStudent.report_grade(name="june",score=43)name
# newStudent.addStudent(name="alex")
# newStudent.addStudent(name="alex")

# newStudent.addStudent(name="alex")


print(d)