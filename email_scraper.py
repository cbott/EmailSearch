import sys
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

def scrape_csv(filename):
    """ Grab names that appear in a csv file, ignoring the first
        column, and only selecting strings that look like names """
    with open(filename, "r") as file:
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
    return names

def remove_duplicates(l):
    """ Remove duplicates from a list and return sorted """
    unique = list(set(l))
    unique.sort()
    return unique

file = sys.argv[1]
people = remove_duplicates(scrape_csv(file))
for person in people:
        print person+","+"/".join(getEmail(person))
