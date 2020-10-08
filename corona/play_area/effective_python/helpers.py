from urllib.parse import parse_qs
my_values=parse_qs('red=5&blue=0&green=',keep_blank_values=True)
print(my_values)
print(repr(my_values))
green=my_values.get("yellow",[""])[0] or 0
print(green)
print((1 and 0))

new_value=my_values.get("bingo",[""])



# one line started   iterators in python

bingo=new_value[0] if new_value[0] else "0"
if new_value[0]:
	print("found")

else:
	print("not found ")
print(new_value)

print(bingo)
def helper_function(values,key):
	# found=values.get(key,["0"])

	red=values.get("red",[""])

	print(values)

	if red[0]:
		return True
	return False

	# print(f'values foudn is {found}')
	
a = ["a" ,"b", "c", "d", "e", "f","g","h"]

# print(a[-7:])
print(a[5:])

d=a[:5]
print(d)
x=1
y=3

# assert d == a 

uncode_char='你好吗?'

f=uncode_char.encode("utf-8")
print(f'the value of is {f}')
reverse_unicode=f[::-1]

# z=reverse_unicode.decode("utf-8")
# print(reverse_unicode)

# assert(x==y,"problems")

numbers=[1,2,3,7,8,5,3]
new_numbers=[x**2 for x in numbers]
rek_numbers=map(lambda x :x**2,new_numbers)
print(rek_numbers)

for item in rek_numbers:
	print(item)

# use list map and filter together
numbers=[3,4,5,7,9,11,12,12]

advanca=map(lambda w:w**2,filter(lambda x:x%2==0,map(lambda v:v**2,numbers)))
aca=list(advanca)

print(aca)
advanca_2=[num**2 for num in [item for item in numbers  if item%2==0]]
print(advanca_2)

# list comprehensions in dictionaries
dicti={1:"alexander",2:"jane",3:"lexas"}
test1=[(key,value) for key,value in dicti.items()]
test2={key:value for key,value in dicti.items()}

test3=((key,value) for key,value in dicti.items())
print(test2)
print(test1)
print(test3)
# f=enumerate(test3)
print(dicti.items())
s=[key for key,value in dicti.items()]
print(s)


length_values=[len(value) for  value in dicti.values()]
print(length_values)

# use list comprehension for map,filter,reduce
numers=[1,2,3,4,5,6,8,8]

# import reduce
from functools import reduce

sumTotal=reduce(lambda x,y:x*y,numers,1)

print(sumTotal)


# trying to flatten array

matrix=[[1,2,3,4],[5,8,7,2],[4,5,62,0],[1,3,4,6]]
flattened=[x**2 for row in matrix   for  x in row]
)

