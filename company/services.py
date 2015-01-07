from models import *

class PersonService:

	def login_auth(self, email, passwd):
		persons = Person.objects.filter(email=email)
		if persons:
			return persons[0]
	
	def current(self, request):
		email = request.session.get('email')
		persons = Person.objects.filter(email=email)
		if persons:
			return persons[0]
