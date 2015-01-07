#encoding=utf8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from chinadaas.services import *

from models import *

def tablelist(request):
	tables = Table.objects.all().order_by('cat__id').order_by('id')

	ctx = ContextService().getContext(request)
	ctx.update(dict(tables=tables))
	return render_to_response('meta/tablelist.html', ctx)

def fieldlist(request, table_id):
	fields = Field.objects.filter(table__id=table_id).order_by('order_no')
	tables = Table.objects.filter(id=table_id)
	ctx = ContextService().getContext(request)
	ctx.update(dict(fields=fields))
	if tables:
		ctx.update(dict(table=tables[0]))
	return render_to_response('meta/fieldlist.html', ctx)
