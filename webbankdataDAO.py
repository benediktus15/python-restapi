import string
from bson import ObjectId

class BankdataDAO(object):

#Initialize our DAO class with the database and set the MongoDB collection we want to use
	def __init__(self, database):
		self.db = database
		self.nasabah = database.nasabah

#This function will handle the finding of names
	def find_nasabah(self,strid=None):
		# gender = 'male'
		if strid:
			q = self.nasabah.find({"_id":ObjectId(strid)})
		else:
			q = self.nasabah.find()
			
		l = []
		for each_nasabah in q:
			l.append({
				'nama':each_nasabah['nama'], 
				'email':each_nasabah['email'], 
				'telepon':each_nasabah['telepon'],
				'tabungan':each_nasabah['tabungan'],
				'umur':each_nasabah['umur'],
				'gender':each_nasabah['gender'],
				'instansi':each_nasabah['instansi'],
				'alamat':each_nasabah['alamat'],
				'aset':each_nasabah['aset'],
				'status':each_nasabah['status'],
				'_id':each_nasabah['_id']
				})

		return l

#This function will handle the insertion of names
	def insert_nasabah(self,nama,email,telepon,umur,instansi,alamat,gender,status,aset,jumlahaset,nilaiaset,tabungan):
		newnasabah = {'nama':nama,
						'email':email,
						'telepon':telepon,
						'tabungan':tabungan,
						'umur':umur,
						'gender':gender,
						'instansi':instansi,
						'alamat':alamat,
						'aset':{'jumlah':jumlahaset,'nama':aset,'nilai':nilaiaset},
						'status':status}
		self.nasabah.insert(newnasabah)

	def edit_nasabah(self,strid,nama,email,telepon,umur,instansi,alamat,gender,status,aset,jumlahaset,nilaiaset,tabungan):
		whereid = {"_id":ObjectId(strid)}
		editnasabah = {'nama':nama,
						'email':email,
						'telepon':telepon,
						'tabungan':tabungan,
						'umur':umur,
						'gender':gender,
						'instansi':instansi,
						'alamat':alamat,
						'aset':{'jumlah':jumlahaset,'nama':aset,'nilai':nilaiaset},
						'status':status}
		self.nasabah.update(whereid,editnasabah)

	def delete_nasabah(self,strid):
		whereid = {"_id":ObjectId(strid)}
		self.nasabah.remove(whereid)
