# Author: Fred Pashley
"""
Developers:

Fred Pashley
down328
MQXO
"""
# License: MIT (see "LICENSE" file)

try:
	with open('version.txt', 'r') as f:
		VERSION = f.read()
except FileNotFoundError:
	VERSION = '0.6 (Stable)'
except Exception as ex:
	print(ex)


import os
import sys
import platform as pt
import socket
import time
import datetime as dt
import pytz
import webbrowser as wb


current_directory = str(os.path.dirname(os.path.realpath(__file__)))

VALIDCOMMANDS = ['help', 'exit', 'cls', 'ip', 'platform', 'time', 'cd', 'open', 'web']
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
					if arguments == []:
						print('For more information on a specific command, type HELP command-name')
						for item in VALIDCOMMANDS_SORTED:
							print(f'{item.upper()}')
						print('\nFor more information on tools see the online documentation.')
					elif len(arguments) > 1:
						print('This command is not supported by the help utility.')
					else:
						help_command = str(arguments[0]).lower()
						if help_command == 'exit':
							print('Quits the CommandPy program (command interpreter).\n\nEXIT')
						elif help_command == 'help':
							print('Provides help information for commands.\n\nHELP [command]\n\n    command - displays help information on that command.')
						elif help_command == 'cls':
							print('Clears the screen.\n\nCLS')
						elif help_command == 'ip':
							print('Shows all IP addresses detected in the network.\n\nIP [/?]\n\n    /n    ... All IPs except localhosts.')
						elif help_command == 'platform':
							print('Platform and hardware information.\n\nPLATFORM')
						elif help_command == 'open':
							print('Open a file, enter full path for different directory, file name for same directory. \n\nOPEN [directory]')
						elif help_command == 'time':
							print('Find the current time and use a timer.\n\nTIME [/?] [amount]\n\n    /s    ... System time (local)\n    /t    ... Takes an amout in seconds (must explicitly say "s") and\n              sleeps for that amount of time.')
						elif help_command == 'web':
							print('Opens a webpage.\n\nWEB [address]')
						elif help_command == 'cd':
							print('Changes the selected directory.\n\nCD [direction/destination]')
				elif command == 'exit':
					quit()	
				elif command == 'open':
					if arguments == []:
						print('You cannot have an empty directory.')
					else:
						openstring = arguments[0]
						if "\\" in openstring:
							try:
								os.startfile(arguments[0])
							except FileNotFoundError:
								print('File not found.')
						else:
							directory = '{}\\{}'.format(
								str(current_directory), openstring)
							try:
								os.startfile(directory)
							except FileNotFoundError:
								print('File not found.')
				elif command == 'cls':
					if os.name == 'nt':
						os.system('cls')
					else:
						os.system('clear')
				elif command == 'ip':
					print('')
					if arguments == []:
						for item in [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]]:
						 	print(f'    {item}')
					elif arguments[0] == '-n':
						for item in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]):
							print(f'    {item}')
				elif command == 'platform':
					if arguments == []:
						print(f'Architecture: {pt.architecture()}')
						print(f'Machine: {pt.machine()}')
						print(f'Platform: {pt.platform()}')
						print(f'Processor: {pt.processor()}')
				elif command == 'time':
					if arguments == []:
						print('\n    {}'.format(str(dt.datetime.utcnow())[:19]))
					elif arguments[0] == '-s':
						print('\n    {}'.format(str(dt.datetime.now())[:19]))
					elif arguments[0] == '-t':
						try:
							amount = str(arguments[1])
							if len(amount) >= 2:
								if amount[-1].lower() == 's':
									time.sleep(int(amount[0]))
								else:
									pass
							else:
								pass
						except IndexError:
							print('You must give an amount of time.')
					elif arguments[0] == '-x':
						print('')
						while True:
							print('    {}'.format(str(dt.datetime.utcnow())[:19]))
							time.sleep(1)
				elif command == 'cd':
					if arguments == []:
						print(current_directory)
					else:
						if str(arguments[0])[0] == '.':
							argument = arguments[0]
							old = current_directory.split('\\')
							try:
								for char in argument:
									if len(old) == 1:
										break
									else:
										del(old[-1])
							except IndexError:
								pass
							finally:
								final = old[0]
								try:
									for x in old[1:]:
										final = '{}\\{}'.format(final, x)
								except IndexError:
									pass
								finally:
									current_directory = final
						else:
							st = f'{current_directory}\\{arguments[0]}'
							chosen_directory = st
							try:
								for x in arguments[1:]:
									chosen_directory = '{} {}'.format(chosen_directory, x)
							except IndexError:
								pass
							finally:
								if os.path.exists(chosen_directory) is False:
									print('Directory not found.')
								else:
									current_directory = chosen_directory
				elif command == 'web':
					if len(arguments)>1:
						print('Invalid address.')
					elif arguments == []:
						try:
							wb.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe').open('google.com')
							print('Opening your browser...')
						except wb.Error:
							print('Opening your browser...')
							wb.open('google.com')
					elif arguments[0] == '-c':
						try:
							wb.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('google.com')
							print('Opening your browser...')
						except wb.Error:
							print('Opening your browser...')
							wb.open('google.com')
					else:
						print(f'Opening {arguments[0]} ...')
						wb.open(arguments[0])
				else:
					pass
			else:
				print("'{}' is not recognized as an internal or external command,\noperable program or batch file.".format(command_original))
