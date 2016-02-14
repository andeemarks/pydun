from colors import green, blue
import textwrap
import os
import string

# There should be no need to look here just yet
# This file is just used for hiding away some details
# that aren't needed.
columns, rows = os.popen('stty size', 'r').read().split()
max_width = int(rows)


def show(text):
    print textwrap.fill(text, max_width)
    return


def get_command():
    print green("\nWhat do you do now? ")
    command = string.lower(raw_input("> "))
    while command not in ['look', 'open', 'help', 'quit']:
        command = string.lower(raw_input("> "))

    return command


def list_commands():
    print blue("\nYou have the following commands available:")
    print blue("- open")
    print blue("- look")
    print blue("- quit")
