#!/usr/bin/python

import sys
filename = sys.argv[1]  #changed from sys.argv[0] by original poster
source = open(filename, 'r').read() + '\n'
compile(source, filename, 'exec')
