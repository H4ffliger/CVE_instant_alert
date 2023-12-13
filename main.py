import crawl
from time import sleep
from search_criteria import importSearchCriteria
from mailsend import authenticateMailAccount, sendMail

lastCVEs = []
searchCriteria = []


def getCVEContext(cveNumber):
	cveContent = crawl.crawlCVE(cveNumber)




def crawlLoop():
	global lastCVEs, searchCriteria
	if(crawl.newCVEsFound(lastCVEs)):
		print("Found new CVEs")
		newCVEs = crawl.crawlCurrentCVEs()
		for cve in newCVEs:
			if cve not in lastCVEs:
				print("Found new CVE: " + cve)
				print("Description: " + crawl.crawlCVE(cve))
				for s in searchCriteria:
					if(s in crawl.crawlCVE(cve).lower()):
						sendMail("CVE Alert " + cve + s, crawl.crawlCVE(cve), "haefligerjoshua@gmail.com")
						print("Mail alert sent")

		lastCVEs = newCVEs
	else:
		print("No new CVEs found")
	sleep(60)
	crawlLoop()






if (__name__ == '__main__'):
	searchCriteria = importSearchCriteria("search.txt")
	lastCVEs = crawl.crawlCurrentCVEs()
	authenticateMailAccount()
	crawlLoop()
	