#encoding=utf8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from models import *

def contact(request):
	ctx = dict(user=request.user)
	persons = Person.objects.all().order_by("user__username")
	ctx.update(dict(persons=persons))
	return render_to_response('company/contact.html', ctx)


def link(request):
	ctx = dict(user=request.user)

	links = Link.objects.all()
	ctx.update(dict(links=links))
	return render_to_response('company/link.html', ctx)


def share(request):
	ctx = dict(user=request.user)

	shares = Share.objects.all().order_by("-created")
	ctx.update(dict(shares=shares))
	return render_to_response('company/share.html', ctx)


def book(request):
	ctx = dict(user=request.user)

	books = Book.objects.all().order_by("id")
	ctx.update(dict(books=books))
	return render_to_response('company/book.html', ctx)

