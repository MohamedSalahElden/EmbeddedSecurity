from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
BLOCKSIZE = 16

class Lab06():
    def __init__(self):
        self.key = b'0123456789ABCDEF'
        self.secret = b"MAHARA_CBC1_2023"

    def pad(self, data, block_size):
        padding_size = block_size - (len(data) % block_size)
        if padding_size == 0:
            return data
        if padding_size == block_size:
            return data
        padded_data = data + bytes([padding_size]) * padding_size
        return padded_data


    def encrypt(self, plaintext , iv):
        plaintext = plaintext + self.secret
        plaintext = self.pad(plaintext , BLOCKSIZE)
        assert len(plaintext) % BLOCKSIZE == 0
        obj1 = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = obj1.encrypt(plaintext)
        return ciphertext