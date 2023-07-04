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

    # def encrypt(self , plaintext):
    #     # take the input from user
        
    #     # make cryptographic AES object
    #     cipher = AES.new(self.key, AES.MODE_ECB)
        
    #     # append secret 
    #     # secret_string = base64_decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK').encode('utf-8')
    #     padded_text = self.custom_pad(plaintext + self.secret , 16)
    #     # print(padded_text)
    #     # encrypt the result in AES ECB mode
    #     ciphertext = cipher.encrypt(padded_text)
    #     # print(ciphertext)
    #     # return the cipher text
    #     return ciphertext
    
    # def pad(self , s):
    #     s += (BLOCKSIZE - (len(s) % BLOCKSIZE))*(chr(BLOCKSIZE - (len(s) % BLOCKSIZE)))
    #     return s
    
    def encrypt(self, plaintext , iv):
        plaintext = plaintext + self.secret
        plaintext = self.pad(plaintext , BLOCKSIZE)
        assert len(plaintext) % BLOCKSIZE == 0
        obj1 = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = obj1.encrypt(plaintext)
        return ciphertext