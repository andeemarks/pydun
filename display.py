from Tkinter import *


class Display:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.title = Label(frame, text="PYDUN - A Python Dungeon-Styled Text Adventure!", font=("Helvetica", 24, "bold"))
        self.title.pack(anchor=N)

        self.output = Text(frame, wrap=WORD, relief=SUNKEN, background="#DDDDDD")
        self.output.pack(anchor=N)
        self.output.insert(END, "(Type 'help' for commands.)\n")

        command_frame = Frame(frame)
        command_frame.pack(anchor=W)

        self.prompt = Label(command_frame, text="What do you want to do now?", foreground="#00AA00", font=("Helvetica", 14, "bold italic"))
        self.prompt.pack(side=LEFT)

        self.command_value = StringVar()
        self.command = Entry(command_frame, textvariable=self.command_value)
        self.command.pack(side=RIGHT)
        self.command.focus_set()
        self.command.bind("<Return>",(lambda event: self.check_command()))

    def check_command(self):
        """Invoked when the return key is entered in the command field"""
        print self.command_value.get()

    def show(self, contents):
        """Update the output with the contents"""
        self.output.insert(END, contents)
