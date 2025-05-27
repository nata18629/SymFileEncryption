import Encryption

class Model:
    def __init__(self):
        self.encryption_option = None
        self.encryption_mode = None
        self.file = None
        self.key = None

    def encrypt_file(self):
        pass

    def get_key(self, file):
        self.key = Encryption.generate_key()
