from scipy.stats import spearmanr

f = open('student_result.csv').readlines()
y1 = []
y2 = []
for l in f:
    tem = l.strip().decode('utf8').split(',')
    assert len(tem) == 7
    y1.append(float(tem[-2]))
    y2.append(float(tem[-1]))
print spearmanr(y1,y2)
