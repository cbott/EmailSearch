from searchumich import getEmail

def format_name(name):
	""" John Doe* -(junk) --> John Doe"""
	res = ""
	for letter in name:
		if letter.isalpha() or letter.isspace() or letter is ".":
			res += letter
		else:
			break
	# names should not have more than 3 spaces: "Sir Bob B. Brown"
	if res.count(" ") > 3:
		res = ""
	return res.strip()

with open("volunteers.csv", "r") as file:
	rows = file.readlines()
	names = []
	for row in rows:
		# first column is labels, not names
		cols = row.split(",")[1:]
		for col in cols:
			if col.strip() == "":
				#ignore empty cells
				continue
			name = format_name(col)
			if(name):
				names.append(name)

unique_people = list(set(names))
unique_people.sort()
for person in unique_people:
	print person+","+getEmail(person)
