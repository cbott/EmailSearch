from requests import post

def getEmail(name):
	url = 'https://mcommunity.umich.edu/mcPeopleService/people/search'
	query = {"searchCriteria":name}

	response = post(url, data = query)
	data = response.json()['person']
	try:
		if len(data) == 0:
			return "UNKNOWN"
		elif len(data) == 1:
			return data[0]['email']
		else:
			candidates = []
			for person in data:
				if person["affiliation"] == "Alumni":
					continue
				candidates.append(person)
			email = candidates[0]["email"]
			if len(candidates) > 1:
				email += "*"
			return email
	except:
		return "UNKNOWN+"

if __name__ == "__main__":
	import sys
	if len(sys.argv) < 2:
		print "Usage: searchumich.py <query>"
	else:
		query = ' '.join(sys.argv[1:])
		print query, ":", getEmail(query)
	