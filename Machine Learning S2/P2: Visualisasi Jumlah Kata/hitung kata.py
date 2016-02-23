import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np

f = open("twitter_tweets.txt","r")
jum_kata = {'python':0,'ruby':0,'javascript':0}
baris = f.readline()
while baris != "":
    if 'python' in baris.lower():
        jum_kata['python'] += 1
    elif 'ruby' in baris.lower():
        jum_kata['ruby'] += 1
    elif 'javascript' in baris.lower():
        jum_kata['javascript'] += 1
    baris = f.readline() #membaca baris
#print "Jumlah kata python :",jum_kata['python']
#print "Jumlah kata ruby :",jum_kata['ruby']
#print "Jumlah kata javascript :",jum_kata['javascript']
legend = ('python','ruby','javascript')
y_pos = np.arange(len(legend))
jumlah = np.array([jum_kata['python'],jum_kata['ruby'],jum_kata['javascript']])

plt.barh(y_pos,jumlah,align='center',alpha=0.4)
plt.yticks(y_pos,legend)
plt.xlabel('Jumlah Kata')
plt.title('Jumlah kata pada data twitter_tweets.txt')
plt.show()