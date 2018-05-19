# -*- coding: utf-8 -*-

from smw import *

apiPoint = ""

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

print(ask["query"]["results"]["Help:Using Elasticsearch store"])
