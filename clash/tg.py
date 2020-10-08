mem={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

v=[1,5,10,50,500,1000]
def hijack(values):
	total=0
	prev=None
	for val in values:
		if prev==None:
			total+=val
			

		elif prev>=val:
			total+=val

		elif prev<val:
			total-=prev
			total+=(val-prev)
			
		prev=val
	return total

def roman_to_numeral(rom):
	rom=rom.upper()
	z=[]
	total=0
	prev=None
	for val in rom:
		z.append(mem[val])
	return hijack(z)

def binary_search(val,target):
	first=0
	last=len(val)
	found=None
	
	while first<=last:
		m=first+((last-first)//2)

		print("found is ",found)
		print("m is ",m)
		if  val[m]<=target:
			found=val[m]
			first=m+1
			
		elif val[m]>target:
			last=m-1
	return found
# 4 11111
# 18 10 5 1 1 1
def numeral_to_roman(val):
	o=[]
	while val>0:
		t=binary_search(v,val)
		o.append(t)
		val=val-t

	return o



def merge(arri):
	if len(arri)>1:
		mid=len(arri)//2
		leftHand=arri[:mid]
		rightHand=arri[mid:]
	i=j=k=0
	while len(leftHand)>i and len(rightHand)>j:
		if leftHand[i]<rightHand[j]:
			arri[k]=leftHand[i]
			i+=1
			k+=1
		else:
			arri[k]=rightHand[j]
			j+=1
			k+=1
	while i<len(leftHand):
		arri[k]=leftHand[i]
		i+=1
		k+=1
	while j<len(rightHand):
		arri[k]=rightHand[i]
		j+=1
		k+=1

	return arri