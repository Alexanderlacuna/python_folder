from flask import Flask,jsonify

app=Flask(__name__)
@app.route("/")
def home():
	return jsonify({"name":"alexander","age":20})
if __name__ == '__main__':
	app.run(port=5000,debug=True)

