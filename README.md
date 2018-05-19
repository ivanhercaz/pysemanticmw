# Pysemanticmw

This is a package to make queries in wikis with [Semantic MediaWiki](https://semantic-mediawiki.org) from its [API](https://semantic-mediawiki.org/w/api.php). This is a read-only package that include:

  - A library to make your own scripts to read a Semantic MediaWiki.
  - A command line client.

## Being developed

At this moment Pysemanticmw is being developed, so it is unastable and it hasn't all its main characteristics finished.

## Roadmap

In order to reach version 1.0 in a stable manner, the following must be met:

  - A Python module with the [special actions](https://github.com/SemanticMediaWiki/SemanticMediaWiki/blob/master/docs/technical/api.md) of Semantic MediaWiki API until before the version 3.0 to build your own scripts. These actions are: `ask`, `askargs`, `smwinfo`, `browsebysubject` and `browsebyproperty`.
  - A command client able to run the special actions mentioned above.
  - Test the command client and the module, and upload it to the Python Package Index (Pypi).
