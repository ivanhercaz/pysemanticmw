# -*- coding: utf-8 -*-

import argparse
from smw import *

config = {
    "apiPoint": "asdads",
}


def main():
    cli = {
        "desc": """Command-line interface to access to the API of a Semantic
                MediaWiki installation. Pending to document...""",
        "api": "access url to the API (e.g. https://semantic-mediawiki.org/w/api.php)",
        "ask": "make a query in ask-language",
        "indent": "number of indents to prettify the JSON result"
    }
    parser = argparse.ArgumentParser(
        description=cli["desc"]
    )
    parser.add_argument("-A", "--api", help=cli["api"])
    parser.add_argument("-a", "--ask", help=cli["ask"])
    parser.add_argument("-i", "--indent", help=cli["indent"])

    args = parser.parse_args()

    if args.api:
        smw = SemanticMediaWiki(args.api)
    elif config["apiPoint"] is not "":
        smw = SemanticMediaWiki(config["apiPoint"])
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
