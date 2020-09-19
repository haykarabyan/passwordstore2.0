import json
from hashlib import sha256
from random import randint
from datetime import date


class File:
    def __init__(self, filename):
        self.filename = filename

    def readFile(self):
        with open(self.filename) as f:
            data = f.read()
            data = json.loads(data)
            return data

    def writeFile(self, data):
        with open(self.filename, 'w') as f:
            f.write(data)

    def fill_the_file(self):
        empty = False
        file = File(self.filename)
        with open(self.filename, 'r') as read_obj:
            # read first character
            one_char = read_obj.read(1)
            # if not fetched then file is empty
            if not one_char:
                empty = True
        if empty:
            with open(self.filename, 'w') as f:
                f.write("[]")


class Answer:
    def __init__(self, text):
        self.text = text

    def get_user_input(self, text):
        self.text = input(text)
        if text == 'exit':
            return

    def answer_is_yes(self):
        if self.text.lower() == 'yes' or self.text.lower() == 'y':
            return True
        return False

    def answer_is_no(self):
        if self.text.lower() == "no" or self.text.lower() == 'n':
            return True
        return False

    def answer_is_change(self):
        if self.text.lower() == "change":
            return True
        return False

    def answer_is_interactive(self):
        if self.text.lower() == "interactive":
            return True
        return False


