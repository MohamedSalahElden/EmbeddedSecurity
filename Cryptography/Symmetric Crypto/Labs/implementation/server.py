from flask import Flask, request
from symmetric_crypto_labs import Lab_01_Block_size_detection
from symmetric_crypto_labs import Lab_02_Mode_detection
from symmetric_crypto_labs import Lab_03_ECB_byte_at_a_time
from symmetric_crypto_labs import Lab_04_CBC_IV_detection
from symmetric_crypto_labs import Lab_05_CBC_bit_flipping
from symmetric_crypto_labs import Lab_06_CBC_byte_at_a_time
from symmetric_crypto_labs import Lab_08_CTR_Bit_flipping

from Crypto.Random import get_random_bytes

CBC_iv = b"maharah tech" + get_random_bytes(4)
CTR_encryptor  = Lab_08_CTR_Bit_flipping.lab08()
app = Flask(__name__)

@app.route('/lab1_algo1', methods=['POST'])
def lab1_alog1_handler():
    input_string_bytes = request.form.get('text').encode()
    encryptor  = Lab_01_Block_size_detection.Lab01_algo1()
    ciphertext = encryptor.encrypt(input_string_bytes)
    hex_str = ' '.join([format(byte, '02x') for byte in ciphertext])
    return str(hex_str)


@app.route('/lab1_algo2', methods=['POST'])
def lab1_alog2_handler():
    input_string_bytes = request.form.get('text').encode()
    encryptor  = Lab_01_Block_size_detection.Lab01_algo2()
    ciphertext = encryptor.encrypt(input_string_bytes)
    hex_str = ' '.join([format(byte, '02x') for byte in ciphertext])
    return str(hex_str)

###########################################################################################

@app.route('/lab2_algo1', methods=['POST'])
def lab2_alog1_handler():
    input_string_bytes = request.form.get('text').encode()
    encryptor  = Lab_02_Mode_detection.Lab02_algo1()
    ciphertext = encryptor.encrypt(input_string_bytes)
    hex_str = ' '.join([format(byte, '02x') for byte in ciphertext])
    return str(hex_str)


@app.route('/lab2_algo2', methods=['POST'])
def lab2_alog2_handler():
    input_string_bytes = request.form.get('text').encode()
    encryptor  = Lab_02_Mode_detection.lab02_algo2()
    ciphertext = encryptor.encrypt(input_string_bytes , CBC_iv)
    hex_str = ' '.join([format(byte, '02x') for byte in ciphertext])
    return str(hex_str)

###########################################################################################

@app.route('/lab3', methods=['POST'])
def lab3_handler():
    input_string_bytes = request.form.get('text').encode()
    encryptor  = Lab_03_ECB_byte_at_a_time.Lab03()
    ciphertext = encryptor.encrypt(input_string_bytes)
    hex_str = ' '.join([format(byte, '02x') for byte in ciphertext])
    # print(hex_str)
    return str(hex_str)


###########################################################################################

@app.route('/lab4_enc', methods=['POST'])
def lab4_enc_handler():
    input_string_bytes = request.form.get('text').encode()
    encryptor  = Lab_04_CBC_IV_detection.lab04()
    ciphertext = encryptor.encrypt(input_string_bytes ,CBC_iv)
    hex_str = ' '.join([format(byte, '02x') for byte in ciphertext])
    return str(hex_str)


@app.route('/lab4_dec', methods=['POST'])
def lab3_dec_handler():
    ciphertext_hex = request.form.get('text')
    ciphertext_bytes = bytes.fromhex(ciphertext_hex.replace(' ', ''))
    decryptor  = Lab_04_CBC_IV_detection.lab04()
    ciphertext = decryptor.decrypt(ciphertext_bytes ,CBC_iv)
    hex_str = ' '.join([format(byte, '02x') for byte in ciphertext])
    return str(hex_str)


###########################################################################################

@app.route('/lab5_generate_cookie', methods=['POST'])
def lab5_generate_cookie_handler():
    input_string_bytes = request.form.get('text').encode()
    encryptor  = Lab_05_CBC_bit_flipping.lab05()
    ciphertext = encryptor.encrypt(input_string_bytes ,CBC_iv)
    hex_str = ' '.join([format(byte, '02x') for byte in ciphertext])
    return str(hex_str)


@app.route('/lab5_login', methods=['POST'])
def lab5_login_handler():
    ciphertext_hex = request.form.get('text')
    ciphertext_bytes = bytes.fromhex(ciphertext_hex.replace(' ', ''))
    decryptor  = Lab_05_CBC_bit_flipping.lab05()
    ciphertext = decryptor.decryptAndCheck(ciphertext_bytes ,CBC_iv)
    hex_str = ' '.join([format(byte, '02x') for byte in ciphertext])
    return str(hex_str)

###########################################################################################
@app.route('/lab6', methods=['POST'])
def lab6_handler():
    input_string_bytes = request.form.get('text').encode()
    encryptor  = Lab_06_CBC_byte_at_a_time.Lab06()
    ciphertext = encryptor.encrypt(input_string_bytes , CBC_iv)
    hex_str = ' '.join([format(byte, '02x') for byte in ciphertext])
    return str(hex_str)


###########################################################################################

@app.route('/lab8_generate_cookie', methods=['POST'])
def lab8_generate_cookie_handler():
    global CTR_encryptor
    input_string_bytes = request.form.get('text').encode()
    ciphertext = CTR_encryptor.encrypt(input_string_bytes, nonce= b'12345678')
    hex_str = ' '.join([format(byte, '02x') for byte in ciphertext])
    return str(hex_str)


@app.route('/lab8_login', methods=['POST'])
def lab8_login_handler():
    global CTR_encryptor
    ciphertext_hex = request.form.get('text')
    ciphertext_bytes = bytes.fromhex(ciphertext_hex.replace(' ', ''))
    ciphertext = CTR_encryptor.decryptAndCheck(ciphertext_bytes , nonce= b'12345678')
    hex_str = ' '.join([format(byte, '02x') for byte in ciphertext])
    return str(hex_str)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)

# docker build -t cryptolab .
# docker run -d -p 5000:5000 cryptolab 