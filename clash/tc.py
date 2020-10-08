def missing():
	x=int(input())
	vals=[int(x) for x in input().split()]
	f=list(sorted(vals))
	for i in range(1,x+1):
		if i not in f:
			print(i)
			break

missing()

class Node
env GUIX_PACKAGE_PATH="/home/kabui/gnu_linux/guix-bioinformatics:/home/kabui/gnu_linux/guix-past/modules" ./pre-inst-env guix install python3-genenetwork2 -p ~/opt/python3-genenetwork2