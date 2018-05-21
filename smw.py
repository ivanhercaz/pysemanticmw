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
        self.info = {
            "apiFormat": "{}{}{} ERROR {}: API URL has bad format".format(c.Back.RED, c.Fore.WHITE, c.Style.BRIGHT, cR),
            "help": "Type {0}python3 smwcli.py -h{1} or {0}python3 smwcli.py --help{1} to know how more about it.".format(c.Style.BRIGHT, cR),
            "200": "connection established succesfully",
            "400": "your request cannot be processed by the server due a client error",
            "404": "the requested resourced could not be found",
            "500": "your request cannot be processed due a server error",
            "503": "the server is temporarily unavailable",
            "catastrophic": "if you don't know why your request get this error, open an issue in Github (https://github.com/ivanhercaz/pysemanticmw/issues)",
        }

    def status(self):
        try:
            request = requests.get(self.apiPoint)
            request.raise_for_status()
            request.status_code

            if request.status_code == 200:
                print("{}{}{} {} {} {}: {}".format(c.Back.GREEN, c.Fore.WHITE, c.Style.BRIGHT, request.status_code, request.reason, cR, self.info["200"]))
                print(self.info["help"])
                pass
            else:
                print("Unknown status code: {}".format(request.status_code))
        except requests.exceptions.HTTPError as HTTPError:
            if request.status_code == 400:
                print("{}{}{} {} {} {}: {}".format(c.Back.RED, c.Fore.WHITE, c.Style.BRIGHT, request.status_code, request.reason, cR, self.info["400"]))
                print(self.info["help"])
                sys.exit()
            if request.status_code == 404:
                print("{}{}{} {} {} {}: {}".format(c.Back.RED, c.Fore.WHITE, c.Style.BRIGHT, request.status_code, request.reason, cR, self.info["404"]))
                print(self.info["help"])
                sys.exit()
            if request.status_code == 500:
                print("{}{}{} {} {} {}: {}".format(c.Back.RED, c.Fore.WHITE, c.Style.BRIGHT, request.status_code, request.reason, cR, self.info["500"]))
                print(self.info["help"])
                sys.exit()
            if request.status_code == 503:
                print("{}{}{} {} {} {}: {}".format(c.Back.RED, c.Fore.WHITE, c.Style.BRIGHT, request.status_code, request.reason, cR, self.info["503"]))
                print(self.info["help"])
                sys.exit()
            else:
                print("Something goes wrong, check the error:")
                print("{}{}{}ERROR {} {}".format(c.Back.RED, c.Fore.WHITE, c.Style.BRIGHT, HTTPError, cR))
                print(self.info["help"])
                sys.exit()
        except requests.exceptions.RequestException as requestError:
            print("{}{}{} Catastrophic error {}: {}".format(c.Back.RED, c.Fore.WHITE, c.Style.BRIGHT, cR, self.info["catastrophic"]))
            print(requestError)
            sys.exit()

    def checkAPI(self, apiPoint):
        self.apiPoint = apiPoint
        apiPattern = re.compile("(http(s)?):\\/\\/(\\w*\\.)?(.*)(\\.\\w*)\\/w\\/api\\.php")
        apiPattern = bool(apiPattern.match(self.apiPoint))

        if apiPattern is False:
            print(self.info["apiFormat"])
            print(self.info["help"])
            # pass
            self.status()
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
