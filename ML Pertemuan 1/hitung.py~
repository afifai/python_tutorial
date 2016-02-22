f = open("indonesiaraya.txt","r") #Membuka file indonesiaraya.txt pada direktori yang sama
baris = f.readline() #definisikan variabel baris dengan baris pertama pada file
hitung = 0 #definisikan variabel hitung = 0
while baris != '': #ketika baris tidak sama dengan baris kosong (teks sudah dibaca habis)
	baris = baris.replace("\n","") #replace new line dengan string kosong
	baris_split = baris.split(" ") #pisahkan string dengan spasi, sehingga membentuk list
	hitung = hitung + baris_split.count("Indonesia") #Hitung kata Indonesia pada setiap list
	baris = f.readline() #Pindah ke baris selanjutnya
print "Jumlah kata Indonesia adalah :",hitung #tampilkan pada layar hasil perhitungan kata Indonesia
