def threshold(arrayGambar):
    balanceAr = []
    newAr = arrayGambar
    for baris in arrayGambar:
        for piksel in baris:
            avgNum = reduce(lambda x,y: x+y, piksel[:3]) / len(piksel[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x+y,balanceAr) / len(balanceAr)
    for baris in newAr:
        for piksel in baris:
            if reduce(lambda x,y: x+y, piksel[:3]) / len(piksel[:3]) > balance:
                piksel[0] = 255
                piksel[1] = 255
                piksel[2] = 255
                piksel[3] = 255
            else:
                piksel[0] = 0
                piksel[1] = 0
                piksel[2] = 0
                piksel[3] = 255
    return newAr