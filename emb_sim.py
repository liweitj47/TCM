#encoding=utf-8
import numpy as np
from scipy.spatial.distance import cosine
from scipy.stats import spearmanr

vec = {}
f_vec = open('medicine_vec.txt').readlines()
for i in range(1,len(f_vec)):
    tem = f_vec[i].decode('utf8').strip().split()
    word = tem[0]
    v = np.array([float(num) for num in tem[1:]])
    vec[word] = v
'''
tem = f_vec[172].decode('utf8').strip().split()
word = tem[0]
v = np.array([float(num) for num in tem[1:]])
vec[word] = v
'''

f = open('select.csv').readlines()
write = open('word2vec_result.csv','w')
y1 = []
y2 = []
for l in f:
    tem = l.decode('utf8').strip().split(',')
    m1 = tem[0]
    m2 = tem[1]
    y1.append(float(tem[-1]))
    if m1 not in vec:
        print(m1)
        vec[m1] = vec[u'乌头']
    c = 1.-cosine(vec[m1],vec[m2])
    y2.append(c)
    write.write((m1+','+m2+','+tem[5]+','+str(c)+'\n').encode('utf8'))
write.close()
print spearmanr(y1,y2)
        
