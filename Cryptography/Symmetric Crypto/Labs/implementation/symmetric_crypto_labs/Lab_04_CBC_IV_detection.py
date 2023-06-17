from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class lab04():
    def __init__(self):
        self.key = b'0123456789ABCDEF'
        

    def pad(self , text):
        pad_length = AES.block_size - (len(text) % AES.block_size)
        padding = bytes([pad_length] * pad_length)
        return text + padding

    def unpad(self, text):
        pad_length = text[-1]
        return text[:-pad_length]

    def encrypt(self , plaintext , iv):
        print(plaintext)
        print("plain text length" , len(plaintext))
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padded_text = self.pad(plaintext)
        print("padded text length" ,len(padded_text))
        ciphertext = cipher.encrypt(padded_text)
        return ciphertext

    def decrypt(self , ciphertext , iv):
        try:
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            plaintext = cipher.decrypt(ciphertext)
            print(plaintext)
            return plaintext
        except:
            return b"this is an error message \"cipher text must be multiple of block size\" "
