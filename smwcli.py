# -*- coding: utf-8 -*-

import argparse
from smw import *

config = {
    "apiPoint": "https://semantic-mediawiki.org/w/api.php",
}


def runQuery(smw, action, query, indent):
    if query is not None:
        query = args.query
    else:
        query = input("Insert the query: ")

    if action == "ask":
        if indent is not None:
            ask = smw.ask(query, indent)
            print(ask)
        else:
            ask = smw.ask(query)
            print(ask)
    elif action == "askargs":
        if indent is not None:
            ask = smw.askArgs(query, indent)
            print(ask)
        else:
            ask = smw.askArgs(query)
            print(ask)


def main():
    cli = {
        "desc": """Command-line interface to access to the API of a Semantic
                MediaWiki installation. Pending to document...""",
        "api": "access url to the API (e.g. https://semantic-mediawiki.org/w/api.php)",
        "ask": "make a query in ask-language",
        "askArgs": "TO DO",
        "query": "TO DO",
        "indent": "number of indents to prettify the JSON result"
    }
    parser = argparse.ArgumentParser(
        description=cli["desc"]
    )
    parser.add_argument("-A", "--api", help=cli["api"])
    parser.add_argument("ask", nargs="?", help=cli["ask"])
    parser.add_argument("askArgs", nargs="?", help=cli["ask"])
    parser.add_argument("-q", "--query", help=cli["query"])
    parser.add_argument("-i", "--indent", help=cli["indent"])

    args = parser.parse_args()

    indent = args.indent
    query = args.query

    if args.api:
        smw = SemanticMediaWiki(args.api)
    elif config["apiPoint"] is not "":
        smw = SemanticMediaWiki(config["apiPoint"])
    else:
        apiPoint = input("Insert the API URL of the Semantic MediaWiki you want to read: ")
        smw = SemanticMediaWiki(apiPoint)

    if args.ask:
        action = "ask"
        runQuery(smw, action, query, indent)
    elif args.askArgs:
        action = "askargs"
        runquery(smw, action, query, indent)
    else:
        print("You must choose an action. Type -h to check the positional arguments")


if __name__ == '__main__':
    main()
