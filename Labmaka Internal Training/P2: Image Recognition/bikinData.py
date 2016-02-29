from PIL import Image
import numpy as np
contohAngka = open('dataset.txt','a')
for angka in range(10):
    for angkalagi in range(1,10):
        print(str(angka)+'.'+str(angkalagi)+'.png')
        dirGambar = 'images/numbers/'+str(angka)+'.'+str(angkalagi)+'.png'
        ei = Image.open(dirGambar)
        eiar = np.array(ei)
        eiarl = str(eiar.tolist())
        
        print eiarl
        tulisData = str(angka)+'::'+eiarl+'\n'
        contohAngka.write(tulisData)