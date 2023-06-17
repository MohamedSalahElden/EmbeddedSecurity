from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class Lab02_algo1():
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

class lab02_algo2():
    def __init__(self):
        self.key = b'0123456789ABCDEF'
        self.iv = get_random_bytes(16)

    def custom_pad(self , data, block_size):
        padding_size = block_size - (len(data) % block_size)
        if padding_size == 0 or padding_size == block_size:
            return data
        padded_data = data + bytes([padding_size]) * padding_size
        return padded_data

    def encrypt(self ,plaintext , iv):
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padded_text = self.custom_pad(plaintext, AES.block_size)
        ciphertext = cipher.encrypt(padded_text)
        return ciphertext
