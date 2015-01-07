#encoding=utf8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from services import *
from company.services import *
import time, hashlib

def index(request):
	ctx = ContextService().getContext(request)
	return render_to_response('index.html', ctx)

def tologin(request):
	request.session['prepath'] = request.META.get('HTTP_REFERER')
	ctx = ContextService().getContext(request)
	if ctx.get('username') and ctx.get('email') and ctx.get('timestamp'):
		return HttpResponseRedirect('/index/')
	return render_to_response('login.html', ctx)

def login(request):
	email = request.POST.get('email')
	passwd = request.POST.get('passwd')
	p = PersonService().login_auth(email, passwd)
	ctx = ContextService().getContext(request)
	if p:
		if not passwd:
			passwd = None
		else:
			passwd = hashlib.md5(passwd).hexdigest()
		if (passwd or p.passwd) and passwd != p.passwd:
			ctx.update(dict(message='登录失败，原因：密码不正确'))
			ctx.update(dict(retry_url='/tologin/'))
			return render_to_response('error.html', ctx)
		request.session['username'] = p.name
		request.session['email'] = p.email
		request.session['timestamp'] = long(time.time())
	else:
		ctx.update(dict(message='登录失败，原因：用户不存在'))
		ctx.update(dict(retry_url='/tologin/'))
		return render_to_response('error.html', ctx)
	prepath = request.session['prepath']
	del request.session['prepath']
	#if prepath:
	#return HttpResponseRedirect(prepath)
	return HttpResponseRedirect('/index/')

def to_change_pwd(request):
	request.session['prepath'] = request.META.get('HTTP_REFERER')
	ctx = ContextService().getContext(request)
	if ctx.get('username') and ctx.get('email') and ctx.get('timestamp'):
		return render_to_response('changepwd.html', ctx)
	return HttpResponseRedirect('/tologin/')
	
def change_pwd(request):
	print request.META.get('HTTP_REFERER')
	old_pwd = request.POST.get('oldpasswd')
	new_pwd = request.POST.get('newpasswd')
	p = PersonService().current(request)
	ctx = ContextService().getContext(request)
	if not old_pwd:
		old_pwd = None
	else:
		old_pwd = hashlib.md5(old_pwd).hexdigest()
	if not new_pwd:
		new_pwd = None
	else:
		new_pwd = hashlib.md5(new_pwd).hexdigest()
	if p:
		if (old_pwd or p.passwd) and old_pwd != p.passwd:
			ctx.update(dict(message='修改密码失败，原因：旧密码不正确'))
			ctx.update(dict(retry_url='/tochangepwd/'))
			return render_to_response('error.html', ctx)
		p.passwd = new_pwd
		p.save()
	else:
		ctx.update(dict(message='修改密码失败，原因：请先登录系统'))
		ctx.update(dict(retry_url='/tologin/'))
		return render_to_response('error.html', ctx)
	prepath = request.session['prepath']
	print prepath
	del request.session['prepath']
	#if prepath:
	#return HttpResponseRedirect(prepath)
	ctx.update(dict(message='已成功修改密码'))
	return render_to_response('success.html', ctx)

def logout(request):
	prepath = request.META.get('HTTP_REFERER')
	ContextService().clearSession(request)
	return HttpResponseRedirect('/index/')

