#encoding=utf-8
import re

def process(constituent):
    pat = re.compile(u'(（.+?）)|(\\(.+?\\))|(第[0-9一二三四五六七八九十]+日)')     # remove brackets, either in English or in Chinese
    meds = re.sub(pat,' ',constituent)
    sep = re.compile(u'、|，|,|:|：|；')
    meds = re.sub(sep,' ',meds)
    meds = meds.split(u'。')
    '''
    if len(meds) > 2:
        print constituent.encode('utf8')
    '''
    meds = meds[0].split(' ')
    return [normalize(med)[0] for med in meds]

def normalize(medicine):
    num_pat = re.compile(u'([0-9\.]+)|([一二三四五六七八九十百]+(两|钱|斤|升|斗|枚|个|分|只|枝|片|条))|(半(两|钱|斤|升|斗|枚|个|分|只|枝|片|条))')     # here remains a big problem for number
    med_dose = re.split(num_pat, medicine)
    if len(med_dose) > 2:
        print medicine.encode('utf8')
    else:
        med = med_dose[0]
        dose = med_dose[1:]
    return med_dose
    
f = open('fangji.tab').readlines()
write = open('fangji.txt','w')
for i in range(len(f)):
    tem = f[i].decode('utf8').strip().split('\t')
    if len(tem) != 2:
        #print i,f[i]
        continue
    name, constituent = tem
    cons = process(constituent)
    write.write((' '.join(cons)).encode('utf8')+'\n')
write.close()

