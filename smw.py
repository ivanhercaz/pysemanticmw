# -*- coding: utf-8 -*-

import re
import requests
import sys


class APIErrors():

    def checkAPI(self, apiPoint):
        apiPattern = re.compile("(http(s)?):\\/\\/(\\w*\\.)?(.*)(\\.\\w*)\\/w\\/api\\.php")
        apiPattern = bool(apiPattern.match(apiPoint))

        if apiPattern is False:
            print("API URL has bad format. Check... [TO-DO]")
            sys.exit()
        else:
            pass


class SemanticMediaWiki():

    def __init__(self, apiPoint):

        self.apiPoint = apiPoint

        self.ACTIONS = {
            "ask": "ask",
            "askA": "askargs",
            "browseProp": "browsebyproperty",
            "browseSubj": "browsebysubject",
            "smwinfo": "smwinfo"
        }

        errors = APIErrors()
        checkAPI = errors.checkAPI(self.apiPoint)

        request = requests.get(self.apiPoint)

        print(request.status_code)
        print(request.headers['content-type'])

    def ask(self, query, format):
        print("Ask action")

        self.action = self.ACTIONS["ask"]
        self.query = query
        self.format = format

        self.params = {
            "format": self.format,
            "query": self.query,
            "action": self.format
        }

        self.request = requests.get(self.apiPoint, params=self.params)

        '''
        Tests:
            print(self.request.url)
            print(self.request.text)
            print("\n\n\n\n")
            print(self.request.json())
            print(self.request.json()["query-continue-offset"])
        '''

        print(self.request.text)


if __name__ == "__main__":
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

                ask = smw.ask(query, "jsonfm")
