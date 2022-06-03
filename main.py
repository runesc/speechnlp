# create a basic flask app that return jsonify response
from flask import Flask, jsonify, request, render_template
from nlp import IA

app = Flask(__name__)

@app.route('/api/iot', methods=['POST'])
def index():
	transcript = request.json['text']

	result = IA(transcript)
	
	if result == 'error' or result == []:
		return jsonify({'code': 500, 'message': 'no command found'})

	response_format = {
		'code': 200,
		'results': [],
		'transcription': transcript
	}

	for result in result:
		response_format['results'].append({ 'intent': result[0], 'confidence': result[1] })

	return jsonify(response_format)


@app.route('/')
def home():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True, port=8080, host='0.0.0.0', ssl_context='adhoc')