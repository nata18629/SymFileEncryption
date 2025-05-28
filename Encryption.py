from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
import secrets
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

BLOCK_SIZE = 16
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENCRYPTED_DIR = os.path.join(BASE_DIR, 'encrypted')
DECRYPTED_DIR = os.path.join(BASE_DIR, 'decrypted')
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

    key = key.ljust(32, b'\0')[:32]
    iv = get_random_bytes(16)

    if mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(padding(input))
        output = ciphertext
    elif mode == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(padding(input))
        output = iv + ciphertext
    elif mode == 'CTR':
        nonce = iv[:8]
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        ciphertext = cipher.encrypt(input)
        output = nonce + ciphertext
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

    key = key.ljust(32, b'\0')[:32]

    if mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
        output = unpadding(cipher.decrypt(input))
    elif mode == 'CBC':
        iv = input[:16]
        ciphertext = input[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        output = unpadding(cipher.decrypt(ciphertext))
    elif mode == 'CTR':
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
