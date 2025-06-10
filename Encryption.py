from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
import os
import secrets
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

BLOCK_SIZE = 16
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENCRYPTED_DIR = os.path.join(BASE_DIR, 'encrypted')
DECRYPTED_DIR = os.path.join(BASE_DIR, 'decrypted')
CORRUPTED_DIR = os.path.join(BASE_DIR, 'corrupted')
KEY_DIR = os.path.join(BASE_DIR, 'keys')

for folder in [ENCRYPTED_DIR, DECRYPTED_DIR, KEY_DIR]:
    os.makedirs(folder, exist_ok=True)

def padding(data):
    return pad(data, BLOCK_SIZE)

def unpadding(data):
    return unpad(data, BLOCK_SIZE)

def encryption(filepath, key, mode):
    try:
        with open(filepath, 'rb') as f:
            input = f.read()
    except Exception as e:
        raise ValueError(f"BLAD: {e}")

    key = sha256(key).digest() #key = sha256(key.encode()).digest() dla stringa
    iv = get_random_bytes(16)

    if mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(padding(input))
        output = b'B' + ciphertext
    elif mode == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(padding(input))
        output = b'C' + iv + ciphertext
    elif mode == 'CTR':
        nonce = iv[:8]
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        ciphertext = cipher.encrypt(input)
        output = b'R' + nonce + ciphertext
    else:
        raise ValueError("NIEZNANY TRYB")

    filepath = os.path.join(ENCRYPTED_DIR, os.path.basename(filepath))
    try:
        with open(filepath, 'wb') as f:
            f.write(output)
    except Exception as e:
        raise ValueError(f"BLAD: {e}")

def decryption(filepath, key, mode):
    try:
        with open(filepath, 'rb') as f:
            input = f.read()
    except Exception as e:
        raise ValueError(f"BLAD: {e}")

    key = sha256(key).digest()     #key = sha256(key.encode()).digest() dla stringa

    mode = chr(input[0])
    input = input[1:]

    if mode == 'B':
        cipher = AES.new(key, AES.MODE_ECB)
        output = unpadding(cipher.decrypt(input))
    elif mode == 'C':
        iv = input[:16]
        ciphertext = input[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        output = unpadding(cipher.decrypt(ciphertext))
    elif mode == 'R':
        nonce = input[:8]
        ciphertext = input[8:]
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        output = cipher.decrypt(ciphertext)
    else:
        raise ValueError("NIEZNANY TRYB")

    filepath = os.path.join(DECRYPTED_DIR, os.path.basename(filepath))
    try:
        with open(filepath, 'wb') as f:
            f.write(output)
    except Exception as e:
        raise ValueError(f"BLAD: {e}")
    
def corrupt(filepath, byte_index=30):
    try:
        with open(filepath, 'rb') as f:
            data = bytearray(f.read())
    except Exception as e:
        raise ValueError(f"BLAD: {e}")

    if byte_index < len(data):
        data[byte_index] ^= 0xFF
        filepath = os.path.join(CORRUPTED_DIR, os.path.basename(filepath))
        try:
            with open(filepath, 'wb') as f:
                f.write(data)
        except Exception as e:
            raise ValueError(f"BLAD: {e}")
    else:
        raise ValueError(f"ZA KROTKI PLIK")


def generate_key():
    random_filename = "key_" + secrets.token_hex(8) + ".txt"
    filepath = os.path.join(KEY_DIR, random_filename)
    key = get_random_bytes(32)
    try:
        with open(filepath, 'wb') as f:
            f.write(key)
    except Exception as e:
        raise ValueError(f"BLAD: {e}")
    return key
