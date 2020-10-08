d=[1,2,3,4,5,6]
# print(dir(d))

def func(iterable):
	for item in iterable:
		yield item

s=func(d)
print(s.__class__)

# using generator list comprehension   by using ()

it=(len(x) for x in  open("./file.txt"))
q="ASDsds"
w=enumerate(q,2)
# you can specify index in python


w=[zip(q,w) for q,w in [1,2,34] and [21,8,9]]