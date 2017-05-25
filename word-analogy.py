#encoding=utf-8
from gensim.models.keyedvectors import KeyedVectors
model = KeyedVectors.load_word2vec_format('medicine_vec.bin',binary=True)


l = [u'干姜',u'甘草']
result =  model.most_similar_cosmul(positive=[u'生姜',u'熟地黄'],negative=[u'生地黄'])
for m in result:
    print m[0].encode('utf8'),m[1]

