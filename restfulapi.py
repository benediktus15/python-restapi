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