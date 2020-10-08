class Animal:
	def __init__(self,kind,legs):
		self.kind=kind
		self.legs=legs


	def  isMammal(self):
		return self.legs >=4

c=Animal("AS",32)

x=lambda v:v**2

print(type(x))
print(type(c))
print(x(3))


















c=Animal("bird",2)

print(c.isMammal())
print(dir(c))



