import os
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
key = b"*#*INSERT KEY HERE*#*"
iv = os.urandom(16)
inputFile = sys.stdin.buffer.read()
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(inputFile) + encryptor.finalize()
print(ciphertext)
