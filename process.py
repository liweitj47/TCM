import numpy as np
import cPickle

de = 200
vec = [np.zeros(de),np.zeros(de)]
word2idx = {'padding':0,'OOV':1}
idx2word = ['padding','OOV']
f_vec = open('medicine_vec.txt').readlines()
for i in xrange(1,len(f_vec)):
    tem = f_vec[i].decode('utf8').strip().split(' ')
    word = tem[0]
    v = np.array([float(num) for num in tem[1:]])
    vec.append(v)
    word2idx[word] = len(word2idx)
    idx2word.append(word)

maxlen = 117
data = []
f = open('fangji.txt').readlines()
for l in f:
    words = l.decode('utf8').strip().split()
    sentence = []
    for word in words:
        if word in word2idx:
            sentence.append(word2idx[word])
        else:
            sentence.append(word2idx['OOV'])
    while len(sentence) < maxlen:
        sentence.append(word2idx['padding'])
    if len(sentence) > maxlen:
        maxlen = len(sentence)
    data.append(np.array(sentence))
print 'max sentence length',maxlen
print 'vocabulary size',len(word2idx)
cPickle.dump((data, vec, word2idx, idx2word), open('medicine.pkl','w'))
