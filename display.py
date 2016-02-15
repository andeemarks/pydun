from Tkinter import *


class Display:
    def __init__(self, master):

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

        self.command_value = StringVar()
        self.command = Entry(command_frame, textvariable=self.command_value)
        self.command.pack(side=RIGHT, expand=True)
        self.command.focus_set()
        self.command.bind("<Return>", (lambda event: self.check_command()))

    def check_command(self):
        """Invoked when the return key is entered in the command field"""
        new_command = self.command_value.get().strip().lower()
        print new_command
        self.show_command(new_command)
        if (new_command == "exit"):
            self.frame.quit

    def show(self, location):
        """Update the output with the contents"""
        self.output.insert(END, location.description)

    def show_command(self, command):
        """Update the output with the contents"""
        self.output.tag_config("COMMAND", foreground="blue", font=("Helvetica", 14, "italic"))
        self.output.insert(INSERT, "\n\n" + command + "\n", ("COMMAND"))
        # self.output.tag_remove("COMMAND",  "1.0", 'end')
