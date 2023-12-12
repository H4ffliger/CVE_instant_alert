

def importSearchCriteria(filename):
	lines = open(filename, "r")
	searchCriteria = []
	for l in lines.readlines():
		searchCriteria.append(l.lower().split(','))


