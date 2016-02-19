from Tkinter import *


class Display:
    def __init__(self, master, handler):
        self.master = master
        self.handler = handler
        self.frame = Frame(master)
        self.frame.pack()

        self.title = Label(self.frame, text="PYDUN - A Python Dungeon-Styled Text Adventure!", font=("Helvetica", 24, "bold"))
        self.title.pack(anchor=N)

        self.output = Text(self.frame, wrap=WORD, relief=SUNKEN, background="#DDDDDD", font=("Times", 14))
        self.output.pack(anchor=N)
        self.output.insert(END, "(Type 'help' for commands.)\n")

        command_frame = Frame(self.frame)
        command_frame.pack(anchor=W)

        self.prompt = Label(command_frame, text="What do you want to do now?", foreground="#00AA00", font=("Helvetica", 14, "bold italic"))
        self.prompt.pack(side=LEFT)

        # Make this field take up more space so it fill the rest of the row?
        self.command_value = StringVar()
        self.command = Entry(command_frame, textvariable=self.command_value)
        self.command.pack(side=RIGHT, expand=True)
        self.command.focus_set()
        self.command.bind("<Return>", (lambda event: self.check_command()))

    def check_command(self):
        """Invoked when the return key is entered in the command field"""
        new_command = self.command_value.get().strip().lower()
        # TODO We should stop invalid commands being shown on the output
        self.show_command(new_command)
        self.handler.process_command(new_command)

    def show_location(self, location):
        """Update the output with the contents"""
        self.show(location.description)

    def show(self, description):
        """Update the output with the contents"""
        self.output.insert(END, description)
        self.output.yview(END)

    def show_command(self, command):
        """Update the output with the contents"""
        self.output.tag_config("COMMAND", foreground="blue", font=("Helvetica", 14, "italic"))
        self.output.insert(INSERT, "\n\n" + command + "\n", ("COMMAND"))
        self.output.yview(END)
