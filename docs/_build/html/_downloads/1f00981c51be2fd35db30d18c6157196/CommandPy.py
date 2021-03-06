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

VALIDCOMMANDS = ['help', 'exit']
VALIDCOMMANDS_SORTED = sorted(VALIDCOMMANDS, key=str.lower)

print('CommandPy [Version {}]\n(c) 2020 Fred Pashley. All rights reserved.'.format(VERSION))

while True:
	option = input('\n{}>'.format(current_directory))

	command_split = option.split()
	if command_split == []:
		pass
	else:
		command = command_split[0]; command_original = command; command = command.lower()
		try:
			arguments = command_split[1:]
		except IndexError as er:
			arguments = []
		finally:
			if command in VALIDCOMMANDS:
				if command == 'help':
					print('For more information on a specific command, type HELP command-name')
					for item in VALIDCOMMANDS_SORTED:
						print(f'{item}')
					print('\nFor more information on tools see the online documentation.')
				elif command == 'exit':
					quit()
				else:
					pass
			else:
				print("'{}' is not recognized as an internal or external command,\noperable program or batch file.".format(command_original))