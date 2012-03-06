from sys import argv

script_fn, doc = argv

fo = open(doc)
print fo.read()
fo.close()
