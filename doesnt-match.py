#encoding=utf-8
from gensim.models.keyedvectors import KeyedVectors
model = KeyedVectors.load_word2vec_format('medicine_vec.bin',binary=True)



#l = [u'干姜',u'生姜',u'高良姜',u'熟地黄']
l = [u'牛黄',u'冰片',u'薄荷',u'附子']
result =  model.doesnt_match(l)
print result.encode('utf8')

