class Mahasiswa:
	total_mahasiswa = 0
	def __init__(self,nama,npm,ipk):
		self.nama = nama
		self.npm = npm
		self.ipk = ipk
		Mahasiswa.total_mahasiswa += 1
		
	def getJumlah(self):
		print "total mahasiswa yang terdaftar adalah :",total_mahasiswa
		return self.total_mahasiswa

	def hitungIPK(self,ips):
		self.ipk = (self.ipk + ips)/2
		print "IPK sekarang adalah : ",self.ipk
		return self.ipk	
	def tampilkanData(self):
		print "Nama\t: ",self.nama
		print "NPM\t: ",self.npm
		print "IPK\t: ",self.ipk
