from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter

class lab08():
    def __init__(self):
        self.key = b'0123456789ABCDEF'
        self.counter=Counter.new(128)
        # self.obj = AES.new(self.key,AES.MODE_CTR,nonce = b'12345678' ,counter=Counter.new(128))
        

    def pad(self , text):
        pad_length = AES.block_size - (len(text) % AES.block_size)
        padding = bytes([pad_length] * pad_length)
        return text + padding

    def unpad(self, text):
        pad_length = text[-1]
        return text[:-pad_length]
    

    def custom_pad(self, data, block_size):
        padding_size = block_size - (len(data) % block_size)
        if padding_size == 0:
            return data
        if padding_size == block_size:
            return data
        padded_data = data + bytes([padding_size]) * padding_size
        return padded_data
    
    def encrypt(self , payload , nonce):
        
        for i in range(len(payload)):
            if (payload[i].to_bytes(1 , 'big') == b"="):
                payload = payload.replace(payload[i].to_bytes(1 , 'big') , b'?')
        print(payload)
        str1 = b"comment1=cooking%20MCs;userdata=" + payload + b";comment2=%20like%20a%20pound%20of%20bacon"
        print(str1)
        padded_text = self.custom_pad(str1 , 16)
            # Create an AES cipher object in CTR mode
        cipher = AES.new(self.key, AES.MODE_CTR, counter=self.counter)

        # Encrypt the plaintext
        ciphertext = cipher.encrypt(padded_text)
        return ciphertext
    

    def decryptAndCheck(self, ciphertext , nonce):
        
        # Create an AES cipher object in CTR mode
        cipher = AES.new(self.key, AES.MODE_CTR, counter=self.counter)

        # Decrypt the ciphertext
        plaintext = cipher.decrypt(ciphertext)
        if b";admin=true;" in plaintext:
            res =  b"logged in as admin"
        else:
            res =  b"logged in as user"
        return res




