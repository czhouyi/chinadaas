from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from hbaseDao import HbaseDao

spliter = ('\x01', '|')

# Create your views here.
def query(request):
    p = request.POST
    g = request.GET
    tablename = None
    rowkey = None
    dao = HbaseDao()
    if p.has_key("tablename") and p["tablename"]:
        tablename = p['tablename']
    if p.has_key("rowkey") and p["rowkey"]:
        rowkey = p['rowkey']
    if tablename is None and g.has_key("tablename") and g["tablename"]:
        tablename = g["tablename"]

    results = None
    if rowkey:
        rowkey = rowkey.replace(spliter[1],spliter[0])
        rowkey = rowkey.encode('utf8')
        results = dao.getRow(tablename, rowkey)
    else:
        results = dao.scan(tablename)

    head = ['rowkey']

    value = []
    if results:
        for r in results:
            for k in r.columns.keys():
                try:
                    head.index(k)
                except ValueError:
                    head.append(k)
        for r in results:
            line = [r.row.replace(spliter[0], spliter[1])]
            for col in head[1:]:
                if r.columns.get(col):
                    line.append(r.columns.get(col).value.replace(spliter[0], spliter[1]))
                else:
                    line.append('')
            value.append(line)
    else:
        head = []

    ctx = dict(user=request.user)
    ctx.update({'tablename':tablename, 'head':head, 'value':value})
    ctx.update(csrf(request))
    return render_to_response('hbase/query.html',ctx)

def table(request):
    dao = HbaseDao()
    ctx = dict(user=request.user)
    ctx.update({'tables' : dao.getTables()})
    return render_to_response('hbase/table.html',ctx)

def guo_query(request):
	p = request.POST
	filename = None
	keyword = None
	if p.has_key("filename") and p["filename"]:
		filename = p['filename']
	if p.has_key("keyword") and p["keyword"]:
		keyword = p['keyword']
	
	ctx = {'filename':filename}
	if filename and keyword:
		d = {}
		ctx.update(d)
	
	ctx.update(csrf(request))
	return render_to_response('hbase/guo.html',ctx)
