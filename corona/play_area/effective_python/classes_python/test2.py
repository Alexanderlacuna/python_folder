

class RegistryBook:
	def __init__(self):
		self._students={}

	def student(self,name):
		if name not in self._students:
			self._students[name]=Student()

		return self._students[name]

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

# create the registry
w=RegistryBook()
p=w.student("alexis").subjects("eng").grades(76)
# p.compute_average()
# s=p.subjects("eng")
# s.grades(76)
# p.subjects("eng")