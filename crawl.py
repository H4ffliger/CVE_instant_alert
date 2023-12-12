import requests



def crawlCVE(cveNumber):
	return requests.get('https://nvd.nist.gov/vuln/detail/' + cveNumber).text.split('<p data-testid="vuln-description">')[1].split('</p><br')[0]


	#ToDo: Get request for cve.org
	#https://www.cve.org/CVERecord?id=CVE-2023-4421


def crawlCurrentCVEs():
	response = requests.get('https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&search_type=all&isCpeNameSearch=false')
	content = response.text.split('tbody>')[1].split('</p>')[:-1]

	cves = []
	for c in content:
		cves.append(c.split('vuln/detail/')[1].split('"')[0])
	return cves

def newCVEsFound(cvesToCompare):
	if(cvesToCompare != crawlCurrentCVEs()):
		return True
	return False



if (__name__ == '__main__'):
	print("Run the main.py. this is only the crawler")
    

