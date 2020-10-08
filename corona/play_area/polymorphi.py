class InputData(object):
	def read(self):
		raise NotImplementedError

class PathInputData(InputData):
	def __init__(self,path):
		super().__init__()
		self._path=path

	def read(self):
		return open(self._path).read()


class Worker(object):
	def __init__(self,input_data):

		self._input_data=input_data
		self._result=None

	def map(self):
		raise NotImplementedError

	def reduce(self):
		raise NotImplementedError

class LineCountWorker(Worker):
	def map(self):
		data=self._input_data.read()
		self.result=data.count("\n")

	def reduce(self,other):
		self.result+=other.result

# get delete update add get_one find find_one query list



# exceptions
class DuplicateaKeyError(Exception):

	def __init__(self,key):

		super().__init__(f'the  key {key} already exists')


class NotFoundError(Exception):
	def __init__(self):
		super().__init__(f'the key does not exists')
class MutabilityMixin(object):

	def add(self,key):

		raise NotImplementedError

	def update(self,key):
		raise NotImplementedError

	def delete(self,key):
		raise NotImplementedError

class QuerableMixin(object):
	def list(self):
		raise NotImplementedError

	def query(self,options):
		raise NotImplementedError

	def find(self,key):
		raise NotImplementedError

class QuerableMutableMixin(MutabilityMixin,QuerableMixin):
	pass


class DataProvider(QuerableMutableMixin):
	# _items={}

	def __init__(self):
		self._items={}

	def add(self,key,item_dict):

		if key in self._items:
			raise DuplicateaKeyError(key)


		self._items[key]=item_dict


	def remove(self,key):
		try:
			# del self._items[key]
			self._items.pop(key)
		except KeyError:
			raise NotFoundError

		return "Success ,200"


	def update(self,key,item_dict):
		if key not in self._items:
			raise NotFoundError

		self._items[key]=item_dict


		return self._items
	@property
	
	def list(self):
		return self._items


	def query(self,options):
		pass

	def find(self,key):
		try:
			item=self._items[key]

		except KeyError:
			raise NotFoundError

		return item

	# def relationship(self,instance_key):


class Database(DataProvider):

	
	def createTable(self,table_name):
		db=DataProvider()

		self.add(table_name,db)

	# def deletable (self,key):
	# 	if key not in  self._items:
	# 		raise NotFoundError


	# 	self._items.pop(key)

	# 	return "200"




	def  ranameTable(self,oldKey,newKey):

		if  oldKey in self._items:
			if newKey in self._items:

				raise DuplicateaKeyError(newKey)




		else:
			raise NotFoundError

	def  update(self,key,item_dict):
		raise NotImplementedError







# data=DataProvider()
# print(data._items)
# data.add(1,{
# 	"name":"alexander",
# 	 "age":"3"
# 	})
# print(data._items)

# print(data.find(1))

# data.update(1,{
# 	"name":"Alexis",
# 	"age":12
# 	})

# data.add(2,{
# 	"name":"junkie",
# 	"age":5
# 	})

# data.remove(1)
# print(data.list)

# static attach method to claseses


# first create a database
# then add a table


myDatabase=Database()
myDatabase.createTable("User")


myDatabase.find("User").add(2,{
	"name":"Alexander",
	"Age":12
	})


print(myDatabase.find("User").list)

# print(myDatabase._items)
myDatabase.createTable("Post")
myDatabase.find("Post").add(1,{
	"title":"hello world",
	 "description":"this is a good book"

	})


print(myDatabase.find("User").list)

print(myDatabase.find("Post").list)

print(myDatabase.list)

# myDatabase.deletable("Post")
# myDatabase.remove("Post")

print(myDatabase.find("User").find(2))

myDatabase.find("Post").add(2,{
	"title":"hello world",
	"decription":"this is another test",
	"Creator":myDatabase.find("User").find(2)
	})

print(myDatabase.find("Post").find(2))

# print(w.list)
# print(dir(table))
'''
you create a relationship between tables 
for instance we have user and post table \

user can have many posts but a post can only be created by one user






'''



class GradeBook(object):
	def __init__(self):
		self._grades={}

	def doesnotExists(self,name):

		if name not in self._grades:
			raise NotFoundError


			


	def addStudent(self,name):
		try:
			self._grades[name]={}

		except KeyError:
			raise DuplicateaKeyError(name)


	def addGrade(self,name,subject,grade):


		self.doesnotExists(name)

		by_subject=self._grades[name]
		grade_subj=by_subject.setdefault(subject,[])
		grade_subj.append(grade)
		


	def removeStudent(self,name):
		self.doesnotExists(name)
		del self._grades[name]


	def computeGrade(self,name):
		self.doesnotExists(name)
		student_by_subj=self._grades[name]
		# subj_value=student_by_subj.k

		total=[]

		for grade in student_by_subj.values():
			total+=grade

		# print(subj_value.values())
		# print(type(subj_value))
		# print(subj_value.items))
		# print(dir(subj_value))


		# for item in subj_value.items:
		# 	print(item)



			

		return sum(total)


	def gradeLength(self,name):
		self.doesnotExists(name)
		student_by_subj=self._grades[name]

		total=[]
		for grade in student_by_subj.values():
			total+=grade
		# subj_value=student_by_subj.values



		return len(total)
		

	def computeAverage(self,name):
		grades=self.computeGrade(name)
		grades_count=self.gradeLength(name)
		return grades/grades_count


	def find(self,name):
		self.doesnotExists(name)
		return self._grades[name]

	@property
	def list(self):
		return self._grades



d=GradeBook()

d.addStudent("Alex")

d.addGrade("Alex","eng",57)
d.addGrade("Alex","math",37)
d.addGrade("Alex","sci",67)
d.addGrade("Alex","geo",97)

w=d.computeGrade("Alex")
print(w)
# d.addGrade("Jinn","kis",43)
# print(d.computeGrade("Alex"))
print(d.computeAverage("Alex"))
print(d.find("Alex"))
# print(d.list)


class Grade(object):
	def __init__(self,score,weight):
		self._score=score
		self._weight=weight

	@property
	def score(self):
		return self._score


	@property
	def weight(self):
		return self._weight
	
	
		

class Subject(object):
	def __init__(self):
		self._grades=[]

	def report_grades(self,score,weight):
		self._grades.append(Grade(score,weight))

	def average_grade(self):

		total,total_weight=0,0
		for grade in self._grades:
			# print(grade,score)
			print(grade.score)
			print(grade.weight)
			total+=grade.score
			# print(total)
			total_weight+=grade.weight


		return total/total_weight


class Students(object):
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


class  Gradebook(object):
	def __init__(self):
		self._students={}

	def student(self,name):
		if name not in self._students:
			self._students[name]=Students()

		return self._students[name]


s=Gradebook()
albert=s.student("Albert Eisten")
math=albert.subject("math")
math.report_grades(80,0.10)
print(math.average_grade())

# w=s.student("Alex")
# q=w.subject("eng")
# q.report_grades(100,3.4)
# q.average_grade()
# print(dir(s))



class Baseclass(object):
	def __init__(self,value):
		self.value=value

class FirstClass(Baseclass):
	def __init__(self,value):

		super().__init__(value)
		self.value*=5

class SecondClass(Baseclass):
	def __init__(self,value):

		super().__init__(value)
		self.value+=2



class TrialClass(SecondClass,FirstClass):
	def __init__(self,value):
		# self.value=value
		super().__init__(value)
		# self.value=value


	def getValue(self):
		return self.value

trial=TrialClass(5)
print(trial.value)
# print(trial.getValue())




