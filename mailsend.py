import smtplib

fromAddress = "cve.mailalert@gmail.com"

s = 0

def authenticateMailAccount():
	global s
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()
	s.starttls()
	s.login(fromAddress, "kohh ctmg wimz fhii")

def sendMail(subject, text, reciver_address):
	global s
	message = 'Subject: {}\n\n{}'.format(subject, text)
	s.sendmail(fromAddress, reciver_address, message)
	s.quit()
	return True
	
	
