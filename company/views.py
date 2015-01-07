#encoding=utf8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from services import *
from chinadaas.services import *

from models import *
from testurl import testurl
from mail import Mail

def personlist(request):
	persons = Person.objects.filter(status='1')

	ctx = ContextService().getContext(request)
	ctx.update(dict(persons=persons))
	return render_to_response('company/personlist.html', ctx)

def linklist(request):
	links = Link.objects.all()

	ctx = ContextService().getContext(request)
	ctx.update(dict(links=links))
	return render_to_response('company/linklist.html', ctx)

def sharelist(request):
	shares = Share.objects.all().order_by("-created")
	
	ctx = ContextService().getContext(request)
	ctx.update(dict(shares=shares))
	return render_to_response('company/sharelist.html', ctx)

def macaddrlist(request):
	macaddrs = MacAddr.objects.all().order_by("person__name")
	macs = []
	ctx = ContextService().getContext(request)
	for macaddr in macaddrs:
		d = {}
		d['person_name'] = macaddr.person.name
		d['wire_ip'] = macaddr.wire_ip
		d['wire_less_ip'] = macaddr.wire_less_ip
		d['has_pro_pm'] = macaddr.has_pro_pm
		d['remark'] = macaddr.remark
		if ctx.get('email') and ctx.get('email') == 'weijiangmeng@chinadaas.com':
			d['wire_mac'] = macaddr.wire_mac
			d['wire_less_mac'] = macaddr.wire_less_mac
		else:
			d['wire_mac'] = '%s*********' % (macaddr.wire_mac[:8],)
			d['wire_less_mac'] = '%s*********' % (macaddr.wire_less_mac[:8],)
		macs.append(d)
	
	ctx.update(dict(macaddrs=macs))
	return render_to_response('company/macaddrlist.html', ctx)

def booklist(request):
	books = Book.objects.all().order_by("name")
	
	ctx = ContextService().getContext(request)
	ctx.update(dict(books=books))
	return render_to_response('company/booklist.html', ctx)

def send_macaddr_mail(request):
	macaddrs = MacAddr.objects.all().order_by("person__name")
	f = open('maclist.csv', 'w')
	f.write('%s,%s,%s,%s,%s,%s,%s\n' % ('姓名','有线IP','有线MAC地址','无线IP','无线MAC地址','是否需要访问生产服务器','备注'))
	for ma in macaddrs:
		flag = None
		if ma.has_pro_pm:
			flag = '是'
		else:
			flag = '否'
		print ma.person.name, ma.wire_ip, ma.wire_mac, ma.wire_less_ip, \
		      ma.wire_less_mac, ma.has_pro_pm, ma.remark
		line = '%s,%s,%s,%s,%s,%s,%s\n' % (ma.person.name, ma.wire_ip, ma.wire_mac, ma.wire_less_ip, \
		ma.wire_less_mac, flag.decode('utf8'), ma.remark)
		print type(line)
		f.write(line.encode('utf8'))
	f.flush()
	f.close()
	m = Mail('smtp.exmail.qq.com', 'yichuanzhou@chinadaas.com', 'dugu9jian')
	m.send('yichuanzhou@chinadaas.com', 'yichuanzhou@chinadaas.com', 'MAC地址分配列表'.decode('utf8'), 'maclist.csv')
	import json
	result = {success: 'true'}
	return HttpResponse(json.dumps(result), mimetype='application/javascript')

def macaddredit(request):
	ctx = {}
	ctx.update(csrf(request))
	return render_to_response('company/macaddredit.html', ctx)

def macaddrsubmit(request):
	id = request.POST.get('id')
	person_name = request.POST.get('person_name')
	wire_ip = request.POST.get('wire_ip')
	wire_mac = request.POST.get('wire_mac')
	wire_less_ip = request.POST.get('wire_less_ip')
	wire_less_mac = request.POST.get('wire_less_mac')
	has_pro_pm = request.POST.get('has_pro_pm')
	remark = request.POST.get('remark')
	
	p = Person.objects.get(name=person_name)
	ma = MacAddr.objects.filter(person__name=person_name)
	
	ctx = {}
	ctx.update(csrf(request))

	if ma and not id:
		return HttpResponseRedirect('/company/macaddrlist')
	macaddr = None
	if id:
		macaddr = MacAddr.objects.get(id)
	else:
		macaddr = MacAddr()
	
	macaddr.person = p
	if wire_ip:
		macaddr.wire_ip = wire_ip
	if wire_mac:
		macaddr.wire_mac = wire_mac
	if wire_less_ip:
		macaddr.wire_less_ip = wire_less_ip
	if wire_less_mac:
		macaddr.wire_less_mac = wire_less_mac
	if has_pro_pm:
		macaddr.has_pro_pm = has_pro_pm
	if remark:
		macaddr.remark = remark

	macaddr.save()

	return HttpResponseRedirect('/company/macaddrlist')
