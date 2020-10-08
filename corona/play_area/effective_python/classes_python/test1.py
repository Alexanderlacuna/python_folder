class DuplicateKey(Exception):
	def __init__(self,key):
		msg=f'the vaue already exists'

		super().__init__(self,msg)


class NotFound(Exception):
	def __init__(self,key):
		msg=f'item with key {key} does exists'
		super().__init__(self,msg)




class RegistryBook:
	_items={}

	def  __init__(self):
		pass
		


	def add_name(self,name):

		self._items[name]=[]

	def add_subject(self,name,value):

		if name in self._items:
			self._items[name].append(value)

		else:
			raise DuplicateKey()


	def average_grade(self,name):
		if self._items[name]:
			count=len(self._items[name])
			summation=sum(self._items[name])

		else:
			return "no item exists"

		return summation/count

	def print_registry(self):
		items=self._items

		for key,val in items.items():
			print(key,val)


class SubjectGrade:
	def __init__(self):
		self.subjects={}

	def addSubject(self,name,value):
		self.subject[name]=value

q=RegistryBook()
q.add_name("alexis")
q.add_name("jews")
q.add_subject("jews",52)
q.add_subject("alexis",43)
q.add_subject("jews",52)
q.add_subject("alexis",43)

q.add_subject("jews",52)
q.add_subject("alexis",43)
q.add_subject("alexis",78)
q.add_name("judy")


# q.print_registry()
w=q.average_grade("alexis")
class Subject(object):
	def __init__(self):
		self._grades=[]

	def report_grade(self,score,weight):
		self._grades.append(Grade(score,weight))

	def  average_grade(self):
		total,total_weight=0,0
		for grade in self._grades:
			total+=grade.score*grade.weight
			total_weight+=grade.weight

		return total/total_weight

class Student(object):
	def __init__(self):
		self._subjects={}
	def subject(self,name):
		if name not in self._subjects:
			self._subjects[name]=Subject()

		return self._subjects[name]

	def average_grade(self):
		total,count=0,0
		for subject in self._subjects.values():
			total+=subject.average_grade()
			count+=1

		return total/count

class  GradeBook:
	def __init__(self):
		self._students={}

	def student(self,name):
		if name not in self._students:
			self._students[name]=Student()
		return self._students[name]



# print(w,l)


class GradeBook:
	def __init__(self):
		self._students={}

	def students(self,name):
		if name not in self._students:
			self._students[name]=Subject()

		return self._students[name]

class Subject:
	def __init__(self):
		self._grades=[]

	def report_grade(self,score,weight):
		sel._grades.append(Grade(score,weight))

	def average_grade(self):
		total,total_weight=0,0
		for   grade in self._grades:
			total+=(grade.score*grade.weight)
			total_weight+=grade.weight
		return total/total_weight


class Grade:
	def __init__(self,score,weight):
		self.score=score
		self.weight=weight

class RegistryBook:
	def __init__(self):
		self._students={}

	def student(self,name):
		if name not in self._students:
			self._students[name]=Student()

class Student:
	def __init__(self):
		self._subjects={}

	def subjects(self,name):
		if name not in self._subjects:
			self._subjects[name]=Subject()

		return self._subjects[name]


class Subject:
	def __init__(self):
		self._grades=[]

	def grades(self,value):
		self._grades.append(Grade(value))

	def compute_average(self):
		total=0
		count=0
		for grade in self._grades:
			total+=grade.get_value()
			count+=1

		return total/count


class Grade:
	def __init__(self,value):
		self.value=value


	def get_value(self):
		return self.value

l=GradeBook()

s=l.students("alexis")
print(dir(s))
q=s.subjects("eng")

		






		


