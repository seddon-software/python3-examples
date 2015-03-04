import smtplib
#from smtplib import SMTPException


sender = 'seddon-software@keme.co.uk'
receivers = ['seddon-software@keme.co.uk']

message = """From: From Chris <seddon-software@keme.co.uk>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('smtp.keme.net')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except Exception, e:
   print "Error: unable to send email"



1

