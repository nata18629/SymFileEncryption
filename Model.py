class Model:
    def __init__(self):
        self.encryption_option = None
        self.encryption_mode = None
        self.file = None

    def encrypt_file(self):
        pass

    def generate_key(self):
        pass

    def get_key_from_file(self):
        pass

    def get_key(self, file):
        if file is not None:
            self.key = self.get_key_from_file()
        else:
            self.key = self.generate_key()
