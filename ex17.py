from sys import argv

# EC 3
# As a oneliner without file exists checking or closing the
# files.  Probably bad form here.
open(argv[2], 'w').write(open(argv[1]).read()))
