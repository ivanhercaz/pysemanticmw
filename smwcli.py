# -*- coding: utf-8 -*-

import argparse
from smw import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-A", "--api", help="API URL")
    parser.add_argument("-a", "--ask", help="make a query in ask-language")
    parser.add_argument("-i", "--indent", help="number of indents to prettify the JSON result")

    args = parser.parse_args()

    if args.api:
        smw = SemanticMediaWiki(args.api)

    else:
        apiPoint = input("Insert the API URL of the Semantic MediaWiki you want to read: ")
        smw = SemanticMediaWiki(apiPoint)

    if args.ask:
        if args.indent:
            ask = smw.ask(args.ask, indent=int(args.indent))
            print(ask)
        else:
            ask = smw.ask(args.ask)
            print(ask)

    else:
        query = input("Insert the query: ")
        ask = smw.ask(query)
        if args.indent:
            ask = smw.ask(args.ask, args.indent)
            print(ask)
        else:
            ask = smw.ask(args.ask)
            print(ask)

if __name__ == '__main__':
    main()
