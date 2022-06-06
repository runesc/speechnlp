# create a basic flask app that return jsonify response
from flask import Flask, jsonify, request, render_template
from nlp import IA

app = Flask(__name__)

@app.route('/api/iot', methods=['POST'])
def index():
	transcript = request.json['text']

	# split the transcript into words
	words = transcript.split()
	results = []
	for word in words:
		intent = IA(word) # this returns something like: [ ['value', 'tenis'],  ['product', 0.9013374940145231] ]
		
		if intent != [] and len(intent) > 1:
			obj = {
				'value': intent[0][1],
				'confidence': intent[1][1],
				'intent': intent[1][0]
			}
			results.append(obj)

	response = {
		'code': 200,
		'results': [x for x in results],
		'transcription': transcript
	}

	return jsonify(response)

	"""print(result)
	


	

	response_format = {
		'code': 200,
		'results': [],
		'transcription': transcript
	}

	for result in result:
		response_format['results'].append({ 'intent': result[0], 'confidence': result[1] })



	return jsonify(response_format)"""


@app.route('/')
def home():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True, port=8080, host='0.0.0.0', ssl_context='adhoc')