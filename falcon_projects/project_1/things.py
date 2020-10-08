import falcon
import json
import uuid

# gunicorn -p 8000 --reload app:app

class ItemNotFoundException(Exception):

	def __init__(self, lookup_key):
		msg = f'Item with key {lookup_key} was not found in store'
		super().__init__(msg)

class DuplicateKeyError(Exception):

	def __init__(self, duplicate_key):
		msg = f'Item with key {duplicate_key} already exists'
		super().__init__(msg)

class QueryableMixin(object):

	def find(self, key):
		raise NotImplementedError()

	def list(self, key):
		raise NotImplementedError()

	def query(self, query_options):
		raise NotImplementedError()

class MutatableMixin(object):
	def add(self, key, item):
		raise NotImplementedError()

	def remove(self, key):
		raise NotImplementedError()

	def update(self, key):
		raise NotImplementedError()

class RepositoryMixin(QueryableMixin, MutatableMixin):
	pass

class CSVDataProvider(RepositoryMixin):

	def __init__(self, file_path):
		self_file_path =  file_path

	def find(self, key):
		pass

	def list(self):
		pass 

	def update(self, key, item):
		pass 

	def add(self, key, item):
		pass

	def remove(self, key, item):
		pass

class IllegalOperationError(Exception):

	def __init__(self):
		super.__init__("Operation not permitted!")

class DataProvider(RepositoryMixin):
	_items={

	}

	def add(self, key, item_dict):
		if key in self._items:
			raise DuplicateKeyError(key)
		self._items[key] = item_dict

	def list(self):
		return self._items.values()

	def find(self, key):
		try:
			item =self._items[key]
		except KeyError:
			raise ItemNotFoundException(key)
		return item

	def update(self, key, item_dict):
		if key not in self._items:
			raise ItemNotFoundException(key)
		self._items[key] = item_dict

	def remove(self, key):
		try:
			del self_.items[key]
		except KeyError:
			raise ItemNotFoundException(key)

class Database(DataProvider):


	def __init__(self):
		pass

	def create_table(self, db_name):
		table = DataProvider()
		self.add(db_name, table)


	def list(self):
		return self._items.keys()

	def update(self, key, item_dict):
		raise IllegalOperationError()


		









db = Database()
for table in ['users', 'posts']:
	db.create_table(table)

db.find("users").add("1", {"id":1, "name":"Gaciri", "age": 27})
db.find("users").add("2", {"id":2, "name":"Gaciri", "age": 27})
db.find("posts").add("2234", {"id":2234, "owner_id":"2", "text": "Awesome"})


class ThingCollectionResource(object):

	def on_get(self,req,resp):
		"""handle get requests"""

		resp.status=falcon.HTTP_200
		resp.body="This is the test data"

	def on_post(self,req,resp):

		print(req.context)

		print(req.media)

		createItem={
		"id":str(uuid.uuid4()),
		"name":req.media["name"],
		"age":req.media["age"]

		}

		items.append(createItem)

		resp.status=falcon.HTTP_200
		resp.body=json.dumps(items)



class ThingItemResource(object):

	def __init__(self, db):
		self._db = db
	
	def on_get(self,req,resp,primary_key):
		try:
			resp_data = self._db.find("users").find(primary_key)
		except ItemNotFoundException:
			raise falcon.HTTPNotFound()

		resp.body=json.dumps(resp_data)


	def on_delete(self,req,resp,primary_key):
		pass

		

		


		# items=[item for item in sanizitedItems]





		# v=filter(lambda item:item[id]!=int(primary_key),items)



		# print(items)

		# return json.dumps(items)

		# print(sanizitedItems)
		# try:
		# 	# items=sanizitedItems
			
		# except Exception as e:
		# 	raise e
		# return json.dumps(sanizitedItems)



	










app=falcon.API()


# newThings=ThingCollectionResource()
thing=ThingItemResource(db)




# app.add_route("/things",newThings)
app.add_route("/thing/{primary_key}",thing)

# middlewares 
# hooks
# posts
# serializer



