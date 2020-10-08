from wsgiref.simple_server import make_server

def helloWorld(environ,start_response):
	status='200 OK'
	response_headers=[('Content-type','text/plain')]
	print(environ["REQUEST_METHOD"])

	start_response(status,response_headers)
	return [b'Hello world']




if __name__ == '__main__':
	server=make_server("",5000,helloWorld)
	server.serve_forever()




