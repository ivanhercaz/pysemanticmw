# -*- coding: utf-8 -*-

import argparse
import json
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

    def __init__(self, apiPoint=""):

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

    def ask(self, query, format="json", indent=2):
        print("Ask action")

        self.action = self.ACTIONS["ask"]
        self.query = query
        self.format = format

        self.params = {
            "format": self.format,
            "query": self.query,
            "action": self.action
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

        self.requestResult = self.request.json()
        self.requestResult = json.dumps(self.requestResult, indent=indent)

        return self.requestResult
