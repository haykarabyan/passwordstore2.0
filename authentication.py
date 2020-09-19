from MainFunctions import Answer
from hashlib import sha256

class Authenticate:
    def __init__(self):
        self.text = ''
        self.hash = ''
    def authenticate(self):
        password = Answer('')
        password.get_user_input("Enter your password ")
        if not password:
            return -1
        if password:
            self.hash = self.convert_to_sha256(password)
            with open("hash_password.txt") as f:
                original_hash = f.read()
            if original_hash == self.hash:
                return True

    def update_authentication_password(self):
        new_password = Answer('')
        new_password .get_user_input("Enter your new password ")
        self.hash= self.convert_to_sha256(new_password)

    def convert_to_sha256(self, plain_text):
        h = sha256(bytes(plain_text, 'utf-8'))
        self.hash = h.hexdigest()
        return self.hash