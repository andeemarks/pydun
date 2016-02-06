from colors import red, green, blue
import textwrap
import os

columns, rows = os.popen('stty size', 'r').read().split()
max_width = int(rows)

def show(text):
	print textwrap.fill(text, max_width)
	return

def get_command():
	print green("\nWhat do you do now? ") 
	return raw_input("> ")

def list_commands():
	print blue("\nYou have the following commands available:")
	print blue("- open")
	print blue("- look")
	print blue("- quit")
	

