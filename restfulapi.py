import pymongo
import restReqProcess
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works'})

@app.route('/framework', methods=['GET'])
def returnALL():
	nasabah_list = restReq.find_nasabah()
	return jsonify({'nasabah' : nasabah_list})

@app.route('/framework/detail/<strid>', methods=['GET'])
def returnDetail(strid):
	detail_nasabah = restReq.find_nasabah(strid)
	return jsonify({'nasabah' : detail_nasabah})

@app.route('/framework/add', methods=['POST'])
def returnAdd():
	nama = request.json['nama']
	alamat = request.json['alamat']
	insert_nasabah = restReq.insert_nasabah(nama,alamat)
	return jsonify({'nasabah' : insert_nasabah})
	# test: postman json {'nama' : 'siapa', 'alamat' : 'yogya'}

@app.route('/framework/edit/<strid>', methods=['PUT']) # can use GET as well
def returnEdit(strid):
	nama = request.json['nama']
	alamat = request.json['alamat']
	edit_nasabah = restReq.edit_nasabah(strid,nama,alamat)
	return jsonify({'nasabah' : edit_nasabah})
	# test: postman put url edit/<id>, body json {'nama' : 'siapa', 'alamat' : 'yogya'}

@app.route('/framework/delete/<strid>', methods=['DELETE']) # can use GET as well
def returnDelete(strid):
	delete_nasabah = restReq.delete_nasabah(strid)
	return jsonify({'nasabah' : delete_nasabah})

# S: database
connection_string = "mongodb://localhost:27017" #connection untuk lokal mongo
connection = pymongo.MongoClient(connection_string) #membuat koneksi pymongo
database = connection.bankmo #memilih database, kasus ini #bank
# E: database

# S: modul
restReq = restReqProcess.ReqProcess(database) #membuat objek class
# E: modul

if __name__ == '__main__':
	app.run(debug=True,port=8083)