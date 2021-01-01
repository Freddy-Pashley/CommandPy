# Author: Fred Pashley
"""
Developers:

Fred Pashley
down328
MQXO
"""
# License: MIT (see "LICENSE" file)

import getpass
import webbrowser as wb
import pytz
import datetime as dt
import time
import socket
import platform as pt
import sys
import os


def make_settings():
	if os.path.exists('./settings'): 
		return True
	else:
		os.mkdir('./settings')

		os.mkdir('./settings/directories')
		try:
			open('./settings/directories/sublime_text.txt', 'x')
		except FileExistsError:
			pass
		except:
			pass
		try:
			open('./settings/directories/visual_studio_code.txt', 'x')
		except FileExistsError:
			pass
		except:
			pass
		try:
			open('./settings/directories/minecraft_launcher.txt', 'x')
		except FileExistsError:
			pass
		except:
			pass

		os.mkdir('./settings/user')
		try:
			open('./settings/user/user.txt', 'x')
		except FileExistsError:
			pass
		except:
			pass


try:
	with open('version.txt', 'r') as f:
		VERSION = f.read()
except FileNotFoundError:
	VERSION = '~Error~'
except Exception as ex:
	print(ex)


make_settings()


import sys
import platform as pt
import socket
import time
import datetime as dt
import pytz
import webbrowser as wb
import getpass
import random


current_directory = str(os.path.dirname(os.path.realpath(__file__)))

VALIDCOMMANDS = ['help', 'exit', 'cls', 'ip', 'platform', 'time', 'cd', 'open', 'web', 'settings', 'ping']
VALIDCOMMANDS_SORTED = sorted(VALIDCOMMANDS, key=str.lower)

confirmations = ['okay', 'sure', 'alright']

print('CommandPy [Version {}]\n(c) 2020 Fred Pashley. All rights reserved.'.format(VERSION))

while True:
	f = open('./settings/user/user.txt', 'r')
	data = f.readlines()
	if data == []:
		new = []
		with open('./settings/user/user.txt', 'w') as f:
			a = input('\nHello there! What should I call you? ')
			b = input('What is your age? (We use this to protect you from potentially malicious content and so we are allowed to collect data.) ')
			new.append(f'{a}\n')
			new.append(f'{b}\n')
			f.writelines(new)

	with open('./settings/user/user.txt', 'r') as f:
		data = f.readlines()
		if int(data[1]) < 13:
			print('Due to you being under the age of 13, it is illegal to use this product.\nWe apologise for any inconvenience.')
			time.sleep(10)
			quit()

	option = input('\n{}>'.format(current_directory))

	command_split = option.split()
	if command_split == []:
		pass
	else:
		command = command_split[0]
		command_original = command
		command = command.lower()
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
					elif len(arguments) > 1:S
						print('This command is not supported by the help utility.')
					else:
						help_command = str(arguments[0]).lower()
						if help_command == 'exit':
							print('Quits the CommandPy program (command interpreter).\n\nEXIT')
						elif help_command == 'help':
							print('Provides help information for commands.\n\nHELP [command]\n\n    command - displays help information on that command.')
						elif help_command == 'settings':
							print('Your CommandPy settings.\n\nSETTINGS [/?] [/?] [object]\n\n    clear    ... Factory reset CommandPy.\n                 all, user, directories\n    /m       ... Modify your settings\n                 /u, /d')
						elif help_command == 'cls':
							print('Clears the screen.\n\nCLS')
						elif help_command == 'ip':
							print(
								'Shows all IP addresses detected in the network.\n\nIP [/?]\n\n    /n    ... All IPs except localhosts.')
						elif help_command == 'platform':
							print('Platform and hardware information.\n\nPLATFORM')
						elif help_command == 'open':
							print(
								'Open a file, enter full path for different directory, file name for same directory. \n\nOPEN [/?] [directory]\n\n    /f    ... Opens a file')
						elif help_command == 'time':
							print(
								'Find the current time and use a timer.\n\nTIME [/?] [amount]\n\n    /s    ... System time (local)\n    /t    ... Takes an amout in seconds (must explicitly say "s") and\n              sleeps for that amount of time.')
						elif help_command == 'web':
							print('Opens a webpage.\n\nWEB [address]')
						elif help_command == 'cd':
							print('Changes the selected directory.\n\nCD [direction/destination]')
						elif help_command == 'ping':
							print('Opens cmd.exe and pings the specified address. \n\nPING [IP/Domain]')
				elif command == 'settings':
					if arguments == []:
						print('')
						for filename in os.listdir(r'./settings/user'):
							with open(r'./settings/user/'+filename, 'r') as f:
								a = filename.split('.')
								filename = a[0].title()
								if filename == 'User':
									data = f.readlines()
									print(f'{filename} : {data[0]}Age: {data[1]}')
						for filename in os.listdir(r'./settings/directories'):
							with open(r'./settings/directories/'+filename, 'r') as f:
								a = filename.split('.')
								filename = a[0].title()
								print(f'{filename} : {f.read()}')
					elif arguments[0] == 'clear':
						if arguments[1] == 'all':
							a = input(
								'Confirm you want to factory reset all of your settings? ("Yes/Confirm") ').upper()
							if a == 'YES' or a == 'CONFIRM':
								for filename in os.listdir(f'./settings/user'):
									with open(r'./settings/user/'+filename, 'w'):
										f.close()
								for filename in os.listdir(f'./settings/directories'):
									with open(r'./settings/directories/'+filename, 'w'):
										f.close()
							else:
								pass
						elif arguments[1] == 'user':
							a = input(
								'Confirm you want to factory reset all of your user settings? ("Yes/Confirm") ').upper()
							if a == 'YES' or a == 'CONFIRM':
								for filename in os.listdir(f'./settings/user'):
									with open(r'./settings/user/'+filename, 'w'):
										f.close()
						elif arguments[1] == 'directories':
							a = input(
								'Confirm you want to factory reset all of your directory settings? ("Yes/Confirm") ').upper()
							if a == 'YES' or a == 'CONFIRM':
								for filename in os.listdir(f'./settings/directories'):
									with open(r'./settings/directories/'+filename, 'w'):
										f.close()
					elif arguments[0] == '-m':
						if arguments[1] == '-d':
							directory = arguments[3]
							string = directory
							try:
								for x in arguments[4:]:
									string = f'{string}\\{x}'
								directory = string
							except IndexError:
								pass
							finally:
								if arguments[2] == 'st':
									with open('./settings/directories/sublime_text.txt', 'w') as f:
										f.write(directory)
								elif arguments[2] == 'vsc':
									with open('./settings/directories/visual_studio_code.txt', 'w') as f:
										f.write(directory)
								elif arguments[2] == 'minecraft':
									with open('./settings/directories/minecraft_launcher.txt', 'w') as f:
										f.write(directory)
						elif arguments[1] == '-u':
							if arguments[2] == 'name':
								name = arguments[3]
								with open('./settings/user/user.txt', 'r') as f:
									data = f.readlines()
								data[0] = f'{name}\n'
								with open('./settings/user/user.txt', 'w') as f:
									f.writelines(data)
				elif command == 'exit':
					quit()
				elif command == 'ping':
					os.system(f'ping {arguments[0]}')
				elif command == 'open':
					if arguments[0] == '-f':
						openstring = arguments[0]
						if "\\" in openstring:
							try:
								os.startfile(arguments[0])
								with open('./settings/user/user.txt', 'r') as f:
									name = f.readlines(); name = name[0]; name = name[:-1]
									print(f'{random.choice(confirmations).title()} {name}, opening {arguments[1]}.')
							except FileNotFoundError:
								with open('./settings/user/user.txt', 'r') as f:
									name = f.readlines(); name = name[0]; name = name[:-1]
								print(f"Sorry {name}, but I can't find that file.")
						else:
							directory = '{}\\{}'.format(str(current_directory), arguments[1])
							try:
								os.startfile(directory)
								with open('./settings/user/user.txt', 'r') as f:
									name = f.readlines(); name = name[0]; name = name[:-1]
									print(f'{random.choice(confirmations).title()} {name}, opening {arguments[1]}.')
							except FileNotFoundError:
								with open('./settings/user/user.txt', 'r') as f:
									name = f.readlines(); name = name[0]; name = name[:-1]
								print(f"Sorry {name}, but I can't find that file.")

					else:
						choice = arguments[0].lower()
						if choice == 'st':
							with open('./settings/directories/sublime_text.txt', 'r') as f:
								link = f.read()
								if os.path.exists(link):
									list = link.split('\\')
									if '.' in list[-1]:
										os.startfile(link)
										with open('./settings/user/user.txt', 'r') as f:
											name = f.readlines(); name = name[0]; name = name[:-1]
											print(f'{random.choice(confirmations).title()} {name}, opening Sublime Text.')
									else:
										os.startfile(r'{}\\sublime_text.exe'.format(link))
										with open('./settings/user/user.txt', 'r') as f:
											name = f.readlines(); name = name[0]; name = name[:-1]
											print(f'{random.choice(confirmations).title()} {name}, opening Sublime Text.')
						elif choice == 'vsc':
							with open('./settings/directories/visual_studio_code.txt', 'r') as f:
								link = f.read()
								if os.path.exists(link):
									list = link.split('\\')
									if '.' in list[-1]:
										os.startfile(link)
										with open('./settings/user/user.txt', 'r') as f:
											name = f.readlines(); name = name[0]; name = name[:-1]
											print(f'{random.choice(confirmations).title()} {name}, opening Visual Studio Code.')
									else:
										os.startfile(r'{}\\Code.exe'.format(link))
										with open('./settings/user/user.txt', 'r') as f:
											name = f.readlines(); name = name[0]; name = name[:-1]
											print(f'{random.choice(confirmations).title()} {name}, opening Visual Studio Code.')
						elif choice == 'minecraft':
							with open('./settings/directories/minecraft_launcher.txt', 'r') as f:
								link = f.read()
								if os.path.exists(link):
									list = link.split('\\')
									if '.' in list[-1]:
										os.startfile(link)
										with open('./settings/user/user.txt', 'r') as f:
											name = f.readlines(); name = name[0]; name = name[:-1]
											print(f'{random.choice(confirmations).title()} {name}, opening Minecraft.')
									else:
										os.startfile(r'{}\\MinecraftLauncher.exe'.format(link))
										with open('./settings/user/user.txt', 'r') as f:
											name = f.readlines(); name = name[0]; name = name[:-1]
											print(f'{random.choice(confirmations).title()} {name}, opening Minecraft.')
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
									with open('./settings/user/user.txt', 'r') as f:
											name = f.readlines(); name = name[0]; name = name[:-1]
											print(f"Sorry {name}, but I can't find that directory.")
								else:
									current_directory = chosen_directory
				elif command == 'web':
					if len(arguments)>1:
						with open('./settings/user/user.txt', 'r') as f:
							name = f.readlines(); name = name[0]; name = name[:-1]
							print(f"Sorry {name}, but that is an invalid address.")
					elif arguments == []:
						try:
							wb.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe').open('google.com')
							with open('./settings/user/user.txt', 'r') as f:
								name = f.readlines(); name = name[0]; name = name[:-1]
								print(f"{random.choice(confirmations).title()} {name}, opening your browser.")
						except wb.Error:
							wb.open('google.com')
							with open('./settings/user/user.txt', 'r') as f:
								name = f.readlines(); name = name[0]; name = name[:-1]
								print(f"{random.choice(confirmations).title()} {name}, opening your browser.")
					elif arguments[0] == '-c':
						try:
							wb.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('google.com')
							with open('./settings/user/user.txt', 'r') as f:
								name = f.readlines(); name = name[0]; name = name[:-1]
								print(f"{random.choice(confirmations).title()} {name}, opening your browser.")
						except wb.Error:
							wb.open('google.com')
							with open('./settings/user/user.txt', 'r') as f:
								name = f.readlines(); name = name[0]; name = name[:-1]
								print(f"{random.choice(confirmations).title()} {name}, opening your browser.")
					else:
						wb.open(arguments[0])
						with open('./settings/user/user.txt', 'r') as f:
							name = f.readlines(); name = name[0]; name = name[:-1]
							print(f"{random.choice(confirmations).title()} {name}, opening {arguments[0]}.")
				else:
					pass
			else:
				print("'{}' is not recognized as an internal or external command,\noperable program or batch file.".format(
					command_original))
