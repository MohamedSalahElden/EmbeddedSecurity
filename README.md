# Cryptographic lab
## Hacking the cryptography algorithms


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Welcome to the Cryptographic Lab This lab is dedicated to the exploration and analysis of cryptographic configuration and implementation vulnerabilities, aimed at enhancing the robustness and integrity of cryptographic systems. With eight unique and comprehensive labs, this lab offers an unparalleled learning and research environment for cryptographic enthusiasts, security professionals, and researchers.

## Features

- Eight Symmetric Cryptography Lab with server to test it and exploitation script
- all codes are written in Python
- Docker container is used to run the server


## Installation

CryptoLab requires 
* [Docker](https://www.docker.com/products/docker-desktop/) container to build and run the server
* [Python3](https://www.python.org/downloads/) to run the attacker scripts which attack the cryptographic algorithms on the server

1. Download and Install the dependencies
2. Build and Start the server
   * Pull from docker repository
      * and follow the instructions on ![cryptolab](https://hub.docker.com/r/mohamedsalah5369/cryptolab)
      * or 
         1. pull the image `docker pull mohamedsalah5369/cryptolab`
         2. run the image `docker run -d -p 5000:5000 mohamedsalah5369/cryptolab:latest`
   * Or build it yourself 
       * go to `EmbeddedSecurity\Cryptography\Symmetric Crypto\Labs\implementation`
       * Build the docker image `docker build -t cryptolab .`
       * run the docker container `docker run -d -p 5000:5000 cryptolab`
4. open the `EmbeddedSecurity\Cryptography\Symmetric Crypto\Labs\labCodes\Attacking Symmetric Cryptography systems.ipynb` notebook and start attacking

## How to communicate with the server

to communicate with the server we use `requests` lib in python
```python
import requests

def get_result(lab_name , input_data , byte_object = False):
    try:
        url = f'http://localhost:5000/{lab_name}'
        input_string = input_data
        payload = {'text': input_string}
        response = requests.post(url, data=payload)
        if byte_object == False:
            return response.text
        else:
            return bytes.fromhex(response.text.replace(' ', ''))
    except:
        pass

# example of dealing with the lab environment
print("hex as string" , get_result("lab3" , "plain text"))
print("byte object   " , get_result("lab3" , "plain text" , byte_object=True ))
```
- each lab has it's own path
- some labs may have multiple path representing 2 operations `[ex: /lab4_enc , /lab4_dec]` one for encryption and one for decryption

| Lab Code | Lab Name               | File Name in Docker Image               | path/s           |
|----------|------------------------|----------------------------------------|----------------|
| Lab 00   | Setup                  | -                                      | -              |
| Lab 01   | Block size detection   | Lab_01_Block_size_detection.py         | /lab1_algo1 , /lab1_algo2 |
| Lab 02   | Mode detection         | Lab_02_Mode_detection.py               | /lab2_algo1 , /lab2_algo2          |
| Lab 03   | ECB byte at a time     | Lab_03_ECB_byte_at_a_time.py           | /lab3          |
| Lab 04   | CBC IV detection       | Lab_04_CBC_IV_detection.py             | /lab4_enc , /lab4_dec         |
| Lab 05   | CBC bit flipping       | Lab_05_CBC_bit_flipping.py             | /lab5_generate_cookie , /lab5_login           |
| Lab 06   | CBC byte at a time     | Lab_06_CBC_byte_at_a_time.py           | /lab6          |
| Lab 07   | CBC padding            | Lab_07_CBC_padding.py                  | /lab7          |
| Lab 08   | CTR Bit flipping       | Lab_08_CTR_Bit_flipping.py             | /lab8          |


