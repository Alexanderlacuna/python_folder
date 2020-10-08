# first
# reduc 
d=lambda v:v**2
print(d(2))

names=[("Alexander","kabua"),("Eugene ,MkadsadD"),("David","BeckhamA")]
fullname=(lambda (first,second):first.title().strip() + " " + second.title().strip())
# secondname=(lambda first,second:f"{first.title().strip()} {second.title().strip()}")

# map(fullname,names)

square=[2,3,4,5,6]

rect=[2,3,4,5,1]
square2=[(2,3),(4,1),(6,7)]
sqr=lambda x:x**2
print(map(sqr,square))
sqr2=lambda x,y:x+y
# print(map(sqr2))
d=[x*y for x,y in zip(square,rect)]

# realName=map(lambda (first,second):first.title().strip() + " " + second.title().strip(),names)

c=filter(lambda c :c>4,rect)
print(d)
print(c)

s=reduce(lambda x,y:x*y,rect)
print(s)
