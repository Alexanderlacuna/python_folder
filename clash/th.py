def dfs(graph,start,visited=None):
	if visited is None:
		visited=set()
	visited.add(start)
	print(start)
	for next in graph[start]-visited:
		dfs(graph,next,visited)

	return visited

def dfs2(graph,start,visited=None):
	if  visited is None:
		visited=set()
	visited.add(start)
	for val in graph[start]-visited:
		dfs(graph,val,visited)
	return visited
def bfs(graph,start,visited=None):
	print("Start is ",start)
	traversal=[]
	if visited is None:
		visited=[]
	if start not in visited:
		visited.append(start)
	for  val in graph[start]:
		if val not in visited:
			visited.append(val)
			traversal.append(val)

	
	for val in traversal:
		bfs(graph,val,visited)



	return visited


def dfs3(graph,start,visited=None):
	if visited is None:
		visited=set()
	visited.add(start)
	for val in graph[start]-visited:
		bfs(graph,val,visited)
	return visited
def bsv(graph,start,visited=[]):
	to_visit=[]
	if visited is None:
		visited=[]


	visited.append(start)

	for val 
	


graph={
	'0':set(["1","3"]),
	'1':set(['0','2','4']),
	'2':set(['0']),
	 '3':set(['1']),
	 '4':set(['2','3'])
}



results=dfs(graph,'0')
results2=bsv(graph,"0")
print(results)
print(results2)