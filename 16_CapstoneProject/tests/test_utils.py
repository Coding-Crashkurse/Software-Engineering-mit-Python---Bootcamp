import os
from base64 import urlsafe_b64encode
from hashlib import sha256
from cryptography.fernet import Fernet

from app.utils import hash_password, encrypt_password, decrypt_password, create_env_file


def test_hash_password():
    password = "my_password"
    hashed_password = hash_password(password)
    assert isinstance(hashed_password, bytes)
    assert hashed_password == urlsafe_b64encode(sha256(password.encode()).digest())


def test_encrypt_decrypt_password():
    password = "my_password"

    # Temporarily set the FERNET_KEY environment variable
    os.environ["FERNET_KEY"] = Fernet.generate_key().decode()

    encrypted_password = encrypt_password(password)
    assert encrypted_password != password

    decrypted_password = decrypt_password(encrypted_password)
    assert decrypted_password == password

    # Clean up the temporary environment variable
    del os.environ["FERNET_KEY"]
#
#
def test_create_env_file(mocker):
    env_file = ".env"
    if os.path.exists(env_file):
        os.remove(env_file)

    open_mock = mocker.patch("builtins.open", mocker.mock_open())
    create_env_file()
    open_mock.assert_called_once_with(env_file, "w")

    assert os.path.exists(env_file)
    with open(env_file, "r") as env_file_content:
        content = env_file_content.read()
        assert content.startswith("FERNET_KEY=")

    os.remove(env_file)

