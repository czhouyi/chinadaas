from jpype import *

def guo_query(filename, keyword):
	jvmpath = getDefaultJVMPath()
	jvmpath = '/usr/local/lib/jdk1.7.0_55/jre/lib/amd64/server/libjvm.so'
	if not isJVMStarted():
		startJVM(jvmpath, "-Xint", "-Xmx512m", "-Djava.class.path=guo.jar")
	SvnSearch = JClass('com.ycz.guo.SvnSearch')
	svnsearch = SvnSearch()
	sr = svnsearch.search(filename, keyword)
	result = {}
	result['path'] = sr.getPath()
	result['keyword'] = sr.getKeyword()
	metalist = []
	for meta in sr.getMetas():
		metalist.append({'revision':meta.getRevision(), 'haskey':meta.isHaskey(), 'author':meta.getAuthor(), 'log':meta.getLog()})
	result['metalist'] = metalist
	#shutdownJVM()
	return result
