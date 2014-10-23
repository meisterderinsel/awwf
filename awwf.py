#!/usr/bin/env python3

import sys
import os

from loader import Loader
import loaders

testmode = False


n = 1
while n < len(sys.argv) and sys.argv[n][0] == "-":
	command = sys.argv[n]
	if command == "-test":
		testmode = True
	n += 1


if len(sys.argv) - n != 2:
	print("Usage: %s <url> <file>" % sys.argv[0])
	exit()

url = sys.argv[n]
file = sys.argv[n+1]
if file[0] != "/": file = os.getcwd() + "/" + file


l = Loader.find_loader(url)


if l is None:
	print("No suitable module found for this site")
	exit()


l = l(url,file)
if l.check_out():
	l.print_command()
	if not testmode:
		l.download()
else:
	print("Error")

