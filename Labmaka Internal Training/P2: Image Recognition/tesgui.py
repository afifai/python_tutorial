from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from collections import Counter

def angkaBerapa(filePath):
    matchedAr = []
    loadData = open('dataset.txt','r').read()
    loadData = loadData.split('\n')
    
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()
    
    coba = str(iarl)
    
    for data in loadData:
        try:
            splitData = data.split('::')
            currentNum = splitData[0]
            currentAr = splitData[1]
            
            pikselData = currentAr.split('],')
            pikselCoba = coba.split('],')
            
            x = 0
            while x < len(pikselData):
                if pikselData[x] == pikselCoba[x]:
                    matchedAr.append(int(currentNum))
                    
                x += 1
        except Exception as e:
            print(str(e))
    
    print(matchedAr)
    x = Counter(matchedAr)
    print(x)
    graphX = []
    graphY = []
    
    ylimi = 0
    
    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
        
        
    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3, colspan=4)
    
    ax1.imshow(iar)
    ax2.bar(graphX,graphY,align='center')
    plt.ylim(400)
    
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)
    
    plt.show()
    
angkaBerapa('images/tess.png')