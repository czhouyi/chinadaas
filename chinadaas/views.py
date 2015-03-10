#encoding=utf8
from django.shortcuts import render_to_response

def index(request):
	ctx = dict(user=request.user)
	return render_to_response('index.html', ctx)

def about(request):
	ctx = dict(user=request.user)
	return render_to_response('about.html', ctx)