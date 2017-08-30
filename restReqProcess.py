import string
from bson import ObjectId

class ReqProcess(object):

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
				# 'email':each_nasabah['email'], 
				# 'telepon':each_nasabah['telepon'],
				# 'tabungan':each_nasabah['tabungan'],
				# 'umur':each_nasabah['umur'],
				# 'gender':each_nasabah['gender'],
				# 'instansi':each_nasabah['instansi'],
				'alamat':each_nasabah['alamat'],
				# 'aset':each_nasabah['aset'],
				# 'status':each_nasabah['status'],
				'id':str(each_nasabah['_id'])
				})

		return l

	def insert_nasabah(self,nama,alamat):
		new_nasabah = {
					'nama' : nama,
					'alamat' : alamat
					}

		nasabah_id = self.nasabah.insert(new_nasabah)
		nasabah_baru = self.nasabah.find_one({"_id" : nasabah_id})

		output = ({
			'nama' : nasabah_baru['nama'],
			'alamat' : nasabah_baru['alamat'],
			'id' : str(nasabah_baru['_id'])
			})

		return output