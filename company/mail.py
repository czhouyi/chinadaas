#encoding=gbk
from email.Header import Header
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email import Encoders
import smtplib, datetime

class Mail:

	def __init__(self, smtp_host, user, passwd):
		self.smtp_server = smtplib.SMTP(smtp_host)
		self.smtp_server.login(user, passwd)

	def send(self, fr, to, subject, attach):
		msg = MIMEMultipart()
		att = MIMEText(open(attach, 'rb').read(), 'base64', 'gbk')
		att["Content-Type"] = 'application/octet-stream'
		att["Content-Disposition"] = 'attachment; filename="%s"' % attach
		msg.attach(att)
		#part = MIMEBase('application', 'octet-stream')
		#part.set_payload(open(attach, 'rb').read())
		#Encoders.encode_base64(part)
		#part.add_header('Content-Disposition', 'attachment; filename="%s"' % attach)
		#msg.attach(part)

		msg['to'] = to
		msg['from'] = fr
		msg['subject'] = Header(subject, 'utf8')

		self.smtp_server.sendmail(msg['from'], msg['to'], msg.as_string())

	def __del__(self):
		self.smtp_server.quit()
		self.smtp_server.close()

if __name__ == "__main__":
	mail = Mail('smtp.exmail.qq.com', 'yichuanzhou@chinadaas.com', 'dugu9jian')
	mail.send('yichuanzhou@chinadaas.com', 'yichuanzhou@chinadaas.com', 'maclist.csv', '../maclist.csv')
