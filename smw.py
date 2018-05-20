# -*- coding: utf-8 -*-

import argparse
import colorama as c
import json
import re
import requests
import sys

cR = c.Style.RESET_ALL


class APIErrors():
    def __init__(self):
        self.errors = {
            "apiFormat": "{}{}{} ERROR {}: API URL has bad format".format(c.Back.RED, c.Fore.WHITE, c.Style.BRIGHT, cR),
            "type": "Type {0}python3 smwcli.py -h{1} or {0}python3 smwcli.py --help{1} to know how more about it.".format(c.Style.BRIGHT, cR)
        }

        self.statusCode = {
            "200": "connection established succesfully"
        }


    def status(self):
        request = requests.get(self.apiPoint)

        if request.status_code == 200:
            print("{}{}{} OK {} {}: {}".format(c.Back.GREEN, c.Fore.WHITE, c.Style.BRIGHT, request.status_code, cR, self.statusCode["200"]))
        else:
            print("wrong")


    def checkAPI(self, apiPoint):
        self.apiPoint = apiPoint
        apiPattern = re.compile("(http(s)?):\\/\\/(\\w*\\.)?(.*)(\\.\\w*)\\/w\\/api\\.php")
        apiPattern = bool(apiPattern.match(self.apiPoint))

        if apiPattern is False:
            print(self.errors["apiFormat"])
            print(self.errors["type"])
            sys.exit()
        else:
            self.status()


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

        self.requestResult = self.request.json()
        self.requestResult = json.dumps(self.requestResult, indent=indent)

        return self.requestResult
