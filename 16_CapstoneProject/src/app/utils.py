from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import sha256


def generate_key(password: str) -> bytes:
    return urlsafe_b64encode(sha256(password.encode()).digest())


def encrypt_password(password: str, key: str) -> str:
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password.decode()


def decrypt_password(encrypted_password: str, key: str) -> str:
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password.encode())
    return decrypted_password.decode()
