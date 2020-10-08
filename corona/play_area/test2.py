letters="sdkkfgsidfgquwoamzbvmoituuyyrjjsqoapznASDQWUERIMBOPL"

times=int(input("numbers of times  "))
word=input("Enter the word  ")

_=0

	# char=word[start]


for char in word:



	if char in letters:
		print(f"Give me a letter {char}")

	else:
		print(f'give an letter {char}')






		

print("give me the word")

for  i in range(times):
	print(f"and the word is {word}")
# cuberoot

cube=27
for i in range(int(cube/2)):

	if i**3==cube:
		print(f'that is the answer {i}')

