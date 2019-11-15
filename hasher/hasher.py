import hashlib
# change to password_hasher

class hasher():
    def __init__(self):
        pass

    def sha1(self, string):
        result = hashlib.sha1(string.encode())
        return result.hexdigest()

    def sha256(self, string):
        result = hashlib.sha256(string.encode())
        return result.hexdigest()

    def sha512(self, string):
        result = hashlib.sha512(string.encode())
        return result.hexdigest()
