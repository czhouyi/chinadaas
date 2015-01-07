#encoding=utf-8
from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=60)
    def __unicode__(self):
        return self.name

class Person(models.Model):
	name = models.CharField(max_length=60)
	position = models.ForeignKey(Position)
	phone = models.CharField(max_length=20)
	email = models.EmailField(blank=True)
	qq = models.CharField(max_length=20, blank=True)
	passwd = models.CharField(max_length=20, null=True)
	LEAVE = '0'
	ON = '1'
	STATUS_CHOICES = (
		(LEAVE, '离职'),
		(ON, '在职'),
	)
	status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=ON)
	def __unicode__(self):
		return self.name

class Zone(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Link(models.Model):
    name = models.CharField(max_length=60)
    zone = models.ForeignKey(Zone)
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

class MacAddr(models.Model):
	person = models.ForeignKey(Person)
	wire_ip = models.CharField(max_length=15, null=True)
	wire_mac = models.CharField(max_length=17, null=True)
	wire_less_ip = models.CharField(max_length=15, null=True)
	wire_less_mac = models.CharField(max_length=17, null=True)
	has_pro_pm = models.BooleanField(default=False)
	remark = models.CharField(max_length=100, null=True)
	def __unicode__(self):
		return self.person.name

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
