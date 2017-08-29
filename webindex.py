import bottle
import pymongo
import webbankdataDAO
from bottle import template
import time

#halaman awal, sambil membaca data
@bottle.route('/')
def bankdata_index():
	waktumulai = time.time()
	nasabah_list = bankdata.find_nasabah()
	durasiproses = time.time()-waktumulai
	return bottle.template('index', dict(nasabah = nasabah_list),durasi=durasiproses)

@bottle.route('/detail/<strid>', method='GET') 
def detail_nasabah(strid):
	waktumulai = time.time()
	nasabah_list = bankdata.find_nasabah(strid)
	durasiproses = time.time()-waktumulai
	return bottle.template('detail', dict(nasabah = nasabah_list),durasi=durasiproses)

@bottle.route('/hapus/<strid>', method='GET') 
def edit_nasabah(strid):
	bankdata.delete_nasabah(strid)
	bottle.redirect('/')

@bottle.route('/edit/<strid>', method='GET') 
def edit_nasabah(strid):
	nasabah_list = bankdata.find_nasabah(strid)
	return bottle.template('edit', dict(nasabah = nasabah_list))

@bottle.route('/editnasabah', method='POST')
def edit_prosesnasabah():
	strid = bottle.request.forms.get("strid")
	nama = bottle.request.forms.get("nama")
	email = bottle.request.forms.get("email")
	telepon = bottle.request.forms.get("telepon")
	umur = bottle.request.forms.get("umur")
	instansi = bottle.request.forms.get("instansi")
	alamat = bottle.request.forms.get("alamat")
	gender = bottle.request.forms.get("gender")
	status = bottle.request.forms.get("status")
	aset = bottle.request.forms.get("aset")
	jumlahaset = bottle.request.forms.get("jumlahaset")
	nilaiaset = bottle.request.forms.get("nilaiaset")
	tabungan = bottle.request.forms.get("tabungan")
	bankdata.edit_nasabah(strid,nama,email,telepon,umur,instansi,alamat,gender,status,aset,jumlahaset,nilaiaset,tabungan)
	bottle.redirect('/')

#halaman untuk tambah nasabah
@bottle.route('/tambah')
def tambah_nasabah():
	return bottle.template('tambah')

#aksi input data baru
@bottle.route('/newnasabah', method='POST')
def tambah_prosesnasabah():
	nama = bottle.request.forms.get("nama")
	email = bottle.request.forms.get("email")
	telepon = bottle.request.forms.get("telepon")
	umur = bottle.request.forms.get("umur")
	instansi = bottle.request.forms.get("instansi")
	alamat = bottle.request.forms.get("alamat")
	gender = bottle.request.forms.get("gender")
	status = bottle.request.forms.get("status")
	aset = bottle.request.forms.get("aset")
	jumlahaset = bottle.request.forms.get("jumlahaset")
	nilaiaset = bottle.request.forms.get("nilaiaset")
	tabungan = bottle.request.forms.get("tabungan")
	bankdata.insert_nasabah(nama,email,telepon,umur,instansi,alamat,gender,status,aset,jumlahaset,nilaiaset,tabungan)
	bottle.redirect('/')

# S: database
connection_string = "mongodb://localhost:27017" #connection untuk lokal mongo
connection = pymongo.MongoClient(connection_string) #membuat koneksi pymongo
database = connection.bankmo #memilih database, kasus ini #bank
# E: database

# S: modul
bankdata = webbankdataDAO.BankdataDAO(database) #membuat objek class
# E: modul

bottle.debug(True)
bottle.run(host='localhost', port=8082) 