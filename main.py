from flask import Flask, jsonify, abort, request, make_response, url_for

app = Flask(__name__, static_url_path = "", static_folder = "static")

@app.route('/')
def index():
  return app.send_static_file('index.html')

@app.route('/do_something', methods=['POST'])
def do_something():
	# print dir(request)
	# print vars(request)
	print request.get_json()
	data = request.data
	# print data
	# data["caca"] = "caca"
	return jsonify(data)
	

if __name__ == '__main__':
  app.run()
