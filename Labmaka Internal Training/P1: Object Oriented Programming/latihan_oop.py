class Rekening:
    total_saldo = 0.0
    total_nasabah = 0
    if total_nasabah != 0:
        rerata = total_saldo/total_nasabah
    else:
        rerata = 0
    def __init__(self,nama,norek,saldo):
        self.nama = nama
        self.norek = norek
        self.saldo = saldo
        Rekening.total_saldo += saldo
        Rekening.total_nasabah += 1
    def tambahSaldo(self,jumlah):
        self.saldo += jumlah
        print "%s tambah %d rupiah" %(self.norek,int(jumlah))
        Rekening.total_saldo += jumlah
    def getData(self):
        print "%s,%s" %(self.nama,self.norek)
        
inp = raw_input()
inp = inp.split()
nasabah = []
for i in range(3*int(inp[0])+int(inp[1])):
    statement = raw_input()
    if i < 3*int(inp[0]):
        ke = i%3
        if ke == 0:
            nama = statement
        elif ke == 1:
            norek = statement
        elif ke == 2:
            saldo = float(statement)
            nasabah.append(Rekening(nama,norek,saldo))
    else:
        if 'mean' in statement.lower():
            "rata-rata: %f rupiah" %(Rekening.rerata)
        elif 'tambah' in statement.lower():
            ada = False
            statement = statement.split(" ")
            for nas in nasabah:
                if statement[1] == nas.norek:
                    ada = True
                    nas.tambahSaldo(float(statement[2]))
            if ada == False:
                print "%s tidak ada" %(statement[1])
        elif 'cari' in statement.lower():
            ada = False
            statement = statement.split(" ")
            for nas in nasabah:
                ada = True
                if nas.saldo >= float(statement[1]):
                    nas.getData()
            if ada == False:
                print "tidak ada"
