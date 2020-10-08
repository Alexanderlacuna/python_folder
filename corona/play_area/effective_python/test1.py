# unicodes strings and bytes
def to_str(bytes_or_str):
	if isinstance(bytes_or_str,bytes):
		value=bytes_or_str.decode("utf-8")

	else:
		value=bytes_or_str


	return value

def to_byte(bytes_or_str):
	if isinstance(bytes_or_str,bytes):
		value=bytes_or_str

	else:
		value=bytes_or_str.decode("utf-8")


	return value

a="A"
b="B"

if not a  is b:
	# print("hello")



