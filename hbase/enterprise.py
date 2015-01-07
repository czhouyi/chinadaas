
from hbaseDao import *

enttype=[]
for line in open('enttype','r'):
    if line: enttype.append(line.replace('\n',''))

rs = scan('ENTERPRISEBASEINFOCOLLECT_20140331', 1000)

fw = open('rs.csv','w')

for r in rs:
    rowkey = r.row
    nodenum = rowkey.split('\x01')[0]
    pripid = rowkey.split('\x01')[1]
    if r.columns.get('f:A'):
        cols = r.columns.get('f:A').value.split('\x01')
        if cols[24] == '1':
            try:
                enttype.index(cols[3])
                fw.write('%s-%s\t%s\n' % (nodenum, pripid, cols[0]))
            except ValueError:
                continue

fw.flush()
fw.close()
