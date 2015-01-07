from django.contrib.auth.models import User
from django.core.context_processors import csrf

import time, json

class ContextService:
	def getContext(self, request):
		ctx = {}
		ctx.update(csrf(request))
		username = request.session.get('username')
		email = request.session.get('email')
		timestamp = request.session.get('timestamp')
		if self.check(request):
			ctx.update(dict(username=username,email=email,timestamp=timestamp))
		return ctx

	def clearSession(self, request):
		username = request.session.get('username')
		email = request.session.get('email')
		timestamp = request.session.get('timestamp')

		if username: del request.session['username']
		if email: del request.session['email']
		if timestamp: del request.session['timestamp']
	
	def check(self, request):
		username = request.session.get('username')
		email = request.session.get('email')
		timestamp = request.session.get('timestamp')
		if timestamp and email and username:
			if (long(timestamp)-long(time.time())<10*3600*24l):
				return True
		return False
