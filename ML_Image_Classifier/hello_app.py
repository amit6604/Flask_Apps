from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
	message = request.get_json(force=True)
	name = message['name']
	response = {'greeting' : 'Hello, ' + name + '!'}

	return jsonify(response)

app.run(host='192.168.0.106',debug=True,port=1238)