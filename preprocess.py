#encoding=utf-8
import re

def process(constituent):
    pat = re.compile(u'(（.+?）)|(\\(.+?\\))|(、)')
    meds = re.sub(pat,'',constituent)
    sep = re.compile(u'、')
    meds = re.sub(sep,',',meds)
    meds = meds.split(u'。')
    '''
    if len(meds) > 2:
        print constituent.encode('utf8')
    '''
    comma = re.compile(u'，|,')
    meds = re.split(comma,meds[0])
    return [normalize(med)[0] for med in meds]

def normalize(medicine):
    num_pat = re.compile(u'[0-9\.半]+')
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

