import random
# we have randint random choice

x=[1,2,3,4,5,6,7,8]
s=random.shuffle(x)
print(s)
# print(random.shuffle(x))
random.shuffle(x)
print(random.random()*200)

# 
print(list(range(10)))
random.choices(x,k=10)

# means there choice and choices in python
c=b'alexander'
print(type(c))
d="DASd"
def to_str(byte_or_string):
	if isinstance(byte_or_string,bytes):
		value=byte_or_string.decode('utf-8')
		
	else:
		value=byte_or_string

	return value
def to_byte(byte_or_string):
	if isinstance(byte_or_string,str):
		value=byte_or_string.encode('utf-8')

	else:
		value=byte_or_string

	return value

	# writing helper classes
c=[1,2,3,4,5,6]
for i,color in enumerate(c):
	print(f'{i} -> {color}')

for color in iter(c):
	print(color)


# override
def enum(iterable,start=0):
	count=start
	for elem in iterable:
		yield count,elem
		count+=1


print(enum('dewfwef'))

for item in enum([32,2,3,4,2,1]):
	print(item)

# for i,value in iter("Dewfe",sentinel=5):
# 	print(f'{c}->{value}')

# list comprehension in dictionary
s={"name":"alexander","age":2,"music":"era"}
for k,v in s.items():
	print(k,v)


s=[{f:v} for f,v in s.items()]

print(s)


# filter map and reduce in python
s=map(lambda x:x**2,filter(lambda v:v>3,[12,12,4,3,1,54]))
# a=s.__next__
# print(next(s))
for s,item in enumerate(s):
	print(item)



# print(a)
# print(type(s))