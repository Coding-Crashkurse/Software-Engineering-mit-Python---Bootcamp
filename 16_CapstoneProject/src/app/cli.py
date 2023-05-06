import typer

from typing import Optional
from app.utils import generate_key, encrypt_password, decrypt_password
from app.database import SessionLocal, User, Password

app = typer.Typer()


def get_user_by_username(username: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()
    return user


@app.command()
def create_user(username: str, password: str):
    db = SessionLocal()
    hashed_password = generate_key(password)
    user = User(username=username, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    typer.echo(f"Benutzer {username} wurde erstellt.")


@app.command()
def login(username: str, password: str) -> Optional[str]:
    user = get_user_by_username(username)
    if user is None:
        typer.echo("Benutzername oder Passwort falsch.")
        return None

    if generate_key(password) != user.hashed_password:
        typer.echo("Benutzername oder Passwort falsch.")
        return None

    return user


@app.command()
def create_password(username: str, password: str, title: str, service_username: str, service_password: str):
    user = login(username, password)
    if user is None:
        return

    key = generate_key(password)
    encrypted_password = encrypt_password(service_password, key)

    db = SessionLocal()
    new_password = Password(title=title, username=service_username, encrypted_password=encrypted_password, user_id=user.id)
    db.add(new_password)
    db.commit()
    db.refresh(new_password)
    db.close()

    typer.echo(f"Passwort für {title} wurde erstellt.")


@app.command()
def get_password(username: str, password: str, title: str):
    user = login(username, password)
    if user is None:
        return

    db = SessionLocal()
    stored_password = db.query(Password).filter(Password.title == title, Password.user_id == user.id).first()
    db.close()

    if stored_password is None:
        typer.echo("Passwort nicht gefunden.")
        return

    key = generate_key(password)
    decrypted_password = decrypt_password(stored_password.encrypted_password, key)

    typer.echo(f"Benutzername: {stored_password.username}")
    typer.echo(f"Passwort: {decrypted_password}")