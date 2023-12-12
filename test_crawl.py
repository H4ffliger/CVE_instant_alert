import unittest
from crawl import crawlCurrentCVEs, crawlCVE
from mailsend import authenticateMailAccount, sendMail


class unitTesting(unittest.TestCase):
	def testCVECrawl(self):
		self.assertEqual(len(crawlCurrentCVEs()), 20)
	def testCrawlCVE(self):
		self.assertEqual(crawlCVE('CVE-2018-8343'), 'An elevation of privilege vulnerability exists in the Network Driver Interface Specification (NDIS) when ndis.sys fails to check the length of a buffer prior to copying memory to it, aka &quot;Windows NDIS Elevation of Privilege Vulnerability.&quot; This affects Windows 7, Windows Server 2012 R2, Windows RT 8.1, Windows Server 2012, Windows 8.1, Windows Server 2016, Windows Server 2008 R2, Windows 10, Windows 10 Servers. This CVE ID is unique from CVE-2018-8342.')
	def testSendMail(self):
		authenticateMailAccount()
		self.assertEqual(sendMail("Test Mail", "Test mail from the cve crawler.,", "haefligerjoshua@gmail.com"), True)
		pass

if (__name__ == '__main__'):
	unittest.main()
    