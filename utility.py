from colors import green, blue
import textwrap
import os

columns, rows = os.popen('stty size', 'r').read().split()
max_width = int(rows)


def show(text):
    print textwrap.fill(text, max_width)
    return


def input_command():
    return raw_input("> ").lower().strip()


def get_command():
    print green("\nWhat do you do now? ")
    command = input_command()
    while command not in ['look', 'open', 'help', 'quit']:
        command = input_command()

    return command
