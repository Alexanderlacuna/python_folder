class InputData:

	def __init__(self,name):
		self.name=name
	def read(self):
		raise NotImplementedError


class PathInputData(InputData):
	def __init__(self,path,name):
		super().__init__(name)
		self.path=path

	def read(self):
		return open(self.path).read()


w=PathInputData("https://www.google.com","Alexis")
print(dir(w))
