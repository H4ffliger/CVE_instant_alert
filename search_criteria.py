

def importSearchCriteria(filename):
	lines = open(filename, "r")
	searchCriteria = []
	for l in lines.readlines():
		searchCriteria = l.lower().split(',')
	return searchCriteria


