# Author: Fred Pashley
# License: MIT (see "LICENSE" file)

try:
	with open('version.txt', 'r') as f:
		VERSION = f.read()
except FileNotFoundError:
	VERSION = '~Error~'
except Exception as ex:
	print(ex)


import os

current_directory = str(os.path.dirname(os.path.realpath(__file__)))

print('CommandPy [Version {}]\n(c) 2020 Fred Pashley. All rights reserved.'.format(VERSION))

while True:
	option = input('\n{}>'.format(current_directory))