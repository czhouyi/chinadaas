#encoding=utf-8
from django.db import models

# Create your models here.
class TableCat(models.Model):
	name = models.CharField(max_length=60)
	desc = models.TextField(blank=True, null=True)
	def __unicode__(self):
		return self.name


class Table(models.Model):
	cat = models.ForeignKey(TableCat)
	name = models.CharField(max_length=60)
	alias = models.CharField(max_length=100)
	desc = models.TextField(blank=True, null=True)
	def __unicode__(self):
		return self.name


class Field(models.Model):
	table = models.ForeignKey(Table)
	name = models.CharField(max_length=60)
	alias = models.CharField(max_length=100)
	type = models.CharField(max_length=20)
	order_no = models.IntegerField(blank=True, null=True)
	desc = models.TextField(blank=True, null=True)
	def __unicode__(self):
		return self.name
