#encoding=utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
	user = models.ForeignKey(User)
	phone = models.CharField(max_length=20)
	qq = models.CharField(max_length=20, blank=True)
	def __unicode__(self):
		return self.user.username


class Domain(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=60)
    domain = models.ForeignKey(Domain)
    url = models.CharField(max_length=60)
    desc = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return self.name


class Share(models.Model):
	person = models.ForeignKey(Person)
	topic = models.CharField(max_length=50)
	created = models.DateField()
	attach = models.FileField(upload_to='../static/company/share/uploads', blank=True)
	desc = models.CharField(max_length=100, blank=True)
	def __unicode__(self):
		return self.topic


class BookCat(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name


class Book(models.Model):
	name = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	cat = models.ForeignKey(BookCat)
	owner = models.ForeignKey(Person, blank=True, null=True)
	NORMAL = '0'
	LENT = '1'
	LOST = '2'
	STATUS_CHOICES = (
		(NORMAL, '普通'),
		(LENT, '借出'),
		(LOST, '遗失'),
	)
	status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NORMAL)
	desc = models.TextField(blank=True)
	def __unicode__(self):
		return self.name
