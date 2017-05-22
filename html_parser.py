from bs4 import BeautifulSoup

def extract(tr):
    """
    return :: name, constituent, effect
    """
    td_list = tr.find_all('td')
    if len(td_list) < 4:
        print tr
        return None, None, None
    return td_list[2].string,td_list[3].string,td_list[4].string

html = BeautifulSoup(open('fangji.html'))
write = open('fangji.tab','w')
tr_list = html.find_all('tr')
print 'number of fangji',len(tr_list)
for tr in tr_list[1:]:
    name,constituent,effect = extract(tr)
    if name and constituent:
        write.write((name+'\t'+constituent+'\n').encode('utf8'))
write.close()
