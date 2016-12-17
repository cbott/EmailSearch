from requests import post

def _valid(person):
    # The person is not an alumnus
    aff = person.get("affiliation")
    if aff is None:
        return False
    if aff == "Alumni" or (aff[0] == "Alumni" and not person.get("title")):
        return False
    return True

def getEmail(name):
    url = 'https://mcommunity.umich.edu/mcPeopleService/people/search'
    query = {"searchCriteria":name}

    response = post(url, data = query)
    data = response.json()['person']

    results = []
    try:
        for person in data:
            #print person
            if _valid(person):
                results.append(str(person["email"]))
    except Exception as e:
        results = ["error"]
    finally:
        return results

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print "Usage: searchumich.py <query>"
    else:
        query = ' '.join(sys.argv[1:])
        print query, ":", getEmail(query)
    