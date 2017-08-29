from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{'name':'Java'}, {'name':'Python'}, {'name':'PHP'}]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works'})

@app.route('/lang', methods=['GET'])
def returnALL():
	return jsonify({'languages' : languages})

@app.route('/lang/query=<string:name>', methods=['GET'])
def retrunOne(name):
	lang = [language for language in languages if language['name'] == name]
	if lang :
		return jsonify({'language' : lang[0]})
	else :
		return jsonify({'language' : 'Not Found'})

@app.route('/lang', methods=['POST']) #add
def addOne():
	language = {'name' : request.json['name']}
	languages.append(language)
	return jsonify({'languages' : languages})

@app.route('/lang/edit=<string:name>', methods=['PUT']) #put / edit
def editOne(name):
	lang = [language for language in languages if language['name'] == name]
	lang[0]['name'] = request.json['name']
	return jsonify({'languages' : languages})

@app.route('/lang/delete=<string:name>', methods=['DELETE'])
def removeOne(name):
	lang = [language for language in languages if language['name'] == name]
	languages.remove(lang[0])
	return jsonify({'languages' : languages})

if __name__ == '__main__':
	app.run(debug=True,port=8083)