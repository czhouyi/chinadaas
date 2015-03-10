#encoding=utf8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from models import *

def table(request):
	ctx = dict(user=request.user)

	tables = Table.objects.all().order_by('cat__id').order_by('id')
	ctx.update(dict(tables=tables))
	return render_to_response('meta/table.html', ctx)


def field(request, table_id):
	ctx = dict(user=request.user)

	fields = Field.objects.filter(table__id=table_id).order_by('order_no')
	tables = Table.objects.filter(id=table_id)
	ctx.update(dict(fields=fields))
	if tables:
		ctx.update(dict(table=tables[0]))
	return render_to_response('meta/field.html', ctx)
