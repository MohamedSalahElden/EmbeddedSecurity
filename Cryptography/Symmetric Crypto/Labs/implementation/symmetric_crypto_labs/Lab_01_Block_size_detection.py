from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

class Lab01_algo1():
    def __init__(self):
        self.key = b'0123456789ABCDEF'

    def custom_pad(self , data, block_size):
        padding_size = block_size - (len(data) % block_size)
        if padding_size == 0 or padding_size == block_size:
            return data
        padded_data = data + bytes([padding_size]) * padding_size
        return padded_data

    def encrypt(self , plaintext):
        cipher = AES.new(self.key, AES.MODE_ECB)
        padded_text = self.custom_pad(plaintext , 16)
        ciphertext = cipher.encrypt(padded_text)
        return ciphertext


class Lab01_algo2():
    def __init__(self):
        self.key = b'abcdefgh'

    def custom_pad(self , data, block_size):
        padding_size = block_size - (len(data) % block_size)
        if padding_size == 0 or padding_size == block_size:
            return data
        padded_data = data + bytes([padding_size]) * padding_size
        return padded_data
    

    def encrypt(self , plain_text): 
        cipher = DES.new(self.key, DES.MODE_ECB)
        padded_text = self.custom_pad(plain_text, DES.block_size)
        ciphertext = cipher.encrypt(padded_text)
        return ciphertext
