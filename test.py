# -*- coding: utf-8 -*-

import pysemanticmw as pysmw

apiPoint = ""

while apiPoint == "":
    if not apiPoint:
        apiPoint = input("Insert API URL (e. g., https://sandbox.semantic-mediawiki.org/w/api.php): ")
        if not apiPoint:
            print("You didn't insert any API URL, please, insert one.")
        else:
            print("API URL: {}".format(apiPoint))

            smw = pysmw.SemanticMediaWiki(apiPoint)

query = "[[Modification date::+]]|?Modification date|sort=Modification date|order=desc"

ask = smw.ask(query, format="json")

print(ask)

'''
Test SemanticMediaWiki > ask()

while apiPoint == "":
    if not apiPoint:
        apiPoint = input("Insert API URL (e. g., https://www.semantic-mediawiki.org/w/api.php): ")
        if not apiPoint:
            print("You didn't insert any API URL, please, insert one.")
        else:
            print("API URL: {}".format(apiPoint))

            smw = SemanticMediaWiki(apiPoint)

query = "[[Modification date::+]]|?Modification date|sort=Modification date|order=desc"

ask = smw.ask(query)

print(ask)

'''
