from collections import namedtuple,deque,ChainMap


# NAMED TUPLES

s=namedtuple("name","age")
w=s("das")

# DEQUUE
a=[1,2,3,4,5]
dequed=deque(a)
print(dequed)
dequed.appendleft(7)
dequed.rotate(4)
# print(type(dequed))
print(dequed)

d={
	"name":"alexander",
	"age":21
}

e={
	"name":"gedion",
	"age":32
}

tst=ChainMap(d,e)
tst.new_child({
	"name":"ADs",
	"age":32
	})
print(tst)

# chainmap


# counter

class test(list):

	@property
	def pop(self):
		return "SDA"

class Vectors():
	def  __init__(self,x,y,z=0):

		self._x=x
		self._y=y
		self._z=z
	
	def __add__(self,others):
		total_x=self._x+others._x
		total_y=self._y+others._y
		return Vectors(total_x,total_y)


	def __sub__(self,others):
		sub_x=others._x-self._x
		sub_y+others._y-self._y
		return Vectors(sub_x,sub_y)


	def __call__(self):
		return Vectors(self._x,self._y,self._z)

class Sorter(object):
	def __init__(self,group):
		self.group=group
		self.found=False


	def __call__(self,x):
		if x in self.group:
			self.found=True
			return (0,x)

		return (1,x)


# test
group=[1,2,4,5]
sorter=Sorter(group)
numbers=[1,2,6,6,2,1,8]
# numbers.sort(key+sorter)


	