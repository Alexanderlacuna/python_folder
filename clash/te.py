def factorial(n):
	t=1
	for i in range(1,n+1):
		t*=i
	return t

class DuplicateKey(Exception):
	def __init__(self,key):
		msg=f'the key {key} already exists'
		super().__init__(self,msg)

class NotFound(Exception):
	def __init__(self,key):
		msg=f"key {key} does not exists"
		super().__init__(msg)

class GraphMixins:
	def insert(self,nodes):
		raise NotImplementedError()
	def populate(self,node):
		raise NotImplementedError()


class Graph:
	def __init__(self):
		self.items={}
	def exists(self,node):
		if node in  self.items:
			return True
		raise NotFound(node)

	def __call__(self):
		return self.items
	def insertNode(self,data):
		if data not in self.items:
			self.items[data]=set()
	def insertList(self,nodes):
		for node in nodes:
			if node not in self.items:
				self.items[node]=set()
	def addList(self,node,link):
		if node in self.items and link in  self.items:
			self.items[node].add(link)
		else:
			raise DuplicateKey(f'{node} or {link}')

	def degree(self,node):
		if self.exists:
			return len(self.items[node])



	def showGraph(self):
		return self.items
	def getNode(self,node):
		if node in self.items:
			return f'{node}->{self.items[node]}'
		raise NotFound(node)

class Visited:
	def __init__(self):
		self.visited=[]



	def insert(self,node):
		if node not in visited:
			visited.append(node)


def dfs(graph,start,visited):
	if start not in graph:
		raise NotFound(start)
	if visited is None:
		visited=set()
	visited.add(start)
	for node in graph[start]:
		if node not in visited:
			dfs(graph,node,visited)
	return visited

def bfs(graph,start,visit=Visited()):

	to_visit=[]


	if start not in visit.visited:
		visit.visited.append(start)
	if start not in graph:
		raise NotFound(start)

	for node  in  graph[start]:
		to_visit.append(node)
		visit.visited.append(node)
	for node in to_visit:
		if node not in visit.visited:
			bfs(graph,start,visit.visited)
	return visit.visited










graph={
	'0':set(["1","3"]),
	'1':set(['0','2','4']),
	'2':set(['0']),
	 '3':set(['1']),
	 '4':set(['2','3'])
}


