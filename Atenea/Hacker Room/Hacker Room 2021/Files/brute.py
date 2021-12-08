import os, operator, base64, time
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, pin):
        self.bs = 16
        self.cipher = AES.new(('123456789012' + pin).encode('utf8'), AES.MODE_ECB)

    def encrypt(self, raw):
        #raw = self._pad(raw)
        encrypted = self.cipher.encrypt(raw)
        encoded = base64.b64encode(encrypted)
        return str(encoded, 'utf-8')

    def decrypt(self, raw):
        decoded = base64.b64decode(raw)
        decrypted = self._unpad(self.cipher.decrypt(decoded))
        return decrypted

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

for i in range(10000):
    pin = str(str(i).zfill(4))
    aes = AESCipher(pin)
    enc = 'hmkWr665MHsBx0xB0LqsroxwY/i9Y+bxQMPb4NIPQ0c='
    raw = 'Proyecto Torre Secret raw'
    try:
        if raw == aes.decrypt(enc).decode('utf8'):
            print('The PIN is: {}'.format(pin))
    except:
        pass