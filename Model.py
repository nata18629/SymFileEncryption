import Encryption

class Model:
    def __init__(self):
        self.encryption_option = None
        self.encryption_mode = None
        self.file = None
        self.key = None

    def encrypt_file(self):
        if self.encryption_option=='ENC':
            Encryption.encryption(self.file, self.key, self.encryption_mode)
        else:
            Encryption.decryption(self.file, self.key, self.encryption_mode)
        return True

    def generate_key(self):
        self.key = Encryption.generate_key()

    def get_key(self, file):
        try:
            with open(file, 'rb') as f:
                self.key = bytearray(f.read())
        except Exception as e:
            raise ValueError(f"BLAD: {e}")
