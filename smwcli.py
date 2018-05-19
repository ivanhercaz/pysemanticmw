# -*- coding: utf-8 -*-

import argparse
from smw import *

parser = argparse.ArgumentParser()
parser.add_argument("-A", "--api", help="[mandatory] API URL")
parser.add_argument("-a", "--ask", help="[mandatory] make a query in ask-language")

args = parser.parse_args()

if args.api:
    smw = SemanticMediaWiki(args.api)
else:
    smw = SemanticMediaWiki()

if args.ask:
    ask = smw.ask(args.ask)
    print(ask)
