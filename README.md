# Pysemanticmw

This is a package to make queries in wikis with [Semantic MediaWiki](https://semantic-mediawiki.org) from its [API](https://semantic-mediawiki.org/w/api.php). This is a read-only package that include:

  - A library to make your own scripts to read a Semantic MediaWiki.
  - A command line client.

## Being developed

At this moment Pysemanticmw is being developed, so it is unastable and it hasn't all its main characteristics finished.

## Roadmap

In order to reach version 1.0 in a stable manner, the following must be met:

  - [ ] A Python module with the [special actions](https://github.com/SemanticMediaWiki/SemanticMediaWiki/blob/master/docs/technical/api.md) of Semantic MediaWiki API until before the version 3.0 to build your own scripts. These actions are:
   - [ ] `ask`
   - [ ] `askargs`
   - [ ] `smwinfo`
   - [ ] `browsebysubject`
   - [ ] `browsebyproperty`.
  - [ ] A command client able to run the special actions mentioned above.
  - [ ] Specification of errors that could occur and how solve them.
  - [ ] Documentation: docblocks in functions and comments in the code to explain it (yes, I like very much to explain the code to be easy to understand for anyone, due it has help me in the past and it could help other people).
  - [ ] Test the command client and the module, and upload it to the Python Package Index (Pypi).

Check the roadmap issue (#1)

## Note

Well, this is an adventure for me... It is the first time developing something like this, a Python module and command-line client. At the first time I said myself: "well, I shouldn't program it, I have not the sufficient knowledge to make it". But, at the end I remembered that what I knows about programming is due things like that. The necessity to make something by myself, either academic tasks or for my collaboration in the Wikimedia Movement. But I have never studied any programming language in courses, academies or college, I have only studied it with resources in Internet ([Real Python](https://realpython.com), [Tutorialspoint](https://tutorialspoint.com), [Python Docs](https://python.org), [StackOverflow](https://stackoverflow.com), among many others).

So, keep in mind several things if someone wants to contribute:

  1. If you find some error or know a better way to make something, let me know with an issue or a pull request. I have to learn many things yet.
  2. Please, do not despair if you check the code and find something very odd, ugly or confusing. If you think it about some piece of the code let me know to fix it and learn.
  3. Normally my main principle in programming tasks is to write what I need. This means that at the first time the code can be very ugly or very dirty, because what I search is that it works. Then I will be worry about how to improve the code in technical and visualization aspects.
  4. If you have any advice or comment, let me know, I will be very grateful to learn with you.
