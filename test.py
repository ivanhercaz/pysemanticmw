# -*- coding: utf-8 -*-

import pysemanticmw as pysmw

apiPoint = "https://sandbox.semantic-mediawiki.org/w/api.php"

if not apiPoint:
    apiPoint = input("Insert API URL (e. g., https://sandbox.semantic-mediawiki.org/w/api.php): ")
    if not apiPoint:
        print("You didn't insert any API URL, please, insert one.")
else:
    print("API URL: {}".format(apiPoint))

    smw = pysmw.SemanticMediaWiki(apiPoint)

query = {
    "conditions": "Modification date::+",
    "printouts": "Modification date",
    "parameters": "|".join(["sort=Modification date", "order=desc"])
}

askArgs = smw.askArgs(query, format="json")


print(askArgs)

'''
 # ask()

while apiPoint == "":
    if not apiPoint:
        apiPoint = input("Insert API URL (e. g., https://www.semantic-mediawiki.org/w/api.php): ")
        if not apiPoint:
            print("You didn't insert any API URL, please, insert one.")
        else:
            print("API URL: {}".format(apiPoint))

            smw = pysmw.SemanticMediaWiki(apiPoint)

query = [
    "[[Modification date::+]]",
    "?Modification date",
    "sort=Modification date",
    "order=desc"
]

ask = smw.ask(query)

print(ask)
'''
