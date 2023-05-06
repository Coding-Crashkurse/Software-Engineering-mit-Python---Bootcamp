import os

import typer
from dotenv import load_dotenv
from tabulate import tabulate

from app.database import (
    Password,
    SessionLocal,
    User,
    create_tables,
    get_logged_in_user,
    get_user_by_username,
)
from app.utils import create_env_file, decrypt_password, encrypt_password, hash_password

app = typer.Typer()

load_dotenv()


@app.command()
def init():
    if os.path.exists(".env") and os.path.exists("app.db"):
        typer.echo("Initialisierung bereits abgeschlossen")
        return
    create_env_file()
    create_tables()
    typer.echo("Initialisierung erfolgreich")


@app.command()
def create_user(username: str, password: str):
    db = SessionLocal()
    hashed_password = hash_password(password)
    user = User(username=username, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    typer.echo(f"Benutzer {username} wurde erstellt.")


@app.command()
def login(username: str, password: str):
    db = SessionLocal()
    user = get_user_by_username(username=username, db=db)
    if user is None:
        typer.echo("Benutzername oder Passwort falsch.")
        return

    if hash_password(password) != user.hashed_password:
        typer.echo("Benutzername oder Passwort falsch.")
        return
    user.is_logged_in = True
    db.commit()
    typer.echo("Erfolgreich eingeloggt.")


@app.command()
def logout():
    db = SessionLocal()
    user = get_logged_in_user(db)
    if user is None:
        typer.echo("Du bist nicht eingeloggt.")
        return

    user.is_logged_in = False
    db.commit()
    db.close()
    typer.echo("Erfolgreich ausgeloggt.")


@app.command()
def create_password(title: str, service_username: str, service_password: str):
    db = SessionLocal()
    user = get_logged_in_user(db=db)
    if user is None:
        typer.echo("Bitte melde dich zuerst an.")
        return

    existing_password = (
        db.query(Password)
        .filter(Password.title == title, Password.user_id == user.id)
        .first()
    )
    if existing_password is not None:
        typer.echo("Ein Passwort mit diesem Titel existiert bereits.")
        db.close()
        return

    encrypted_password = encrypt_password(service_password)

    new_password = Password(
        title=title,
        username=service_username,
        encrypted_password=encrypted_password,
        user_id=user.id,
    )
    db.add(new_password)
    db.commit()
    db.refresh(new_password)
    db.close()

    typer.echo(f"Passwort für {title} wurde erstellt.")


@app.command()
def get_passwords():
    db = SessionLocal()
    user = get_logged_in_user(db)
    if user is None:
        typer.echo("Bitte melde dich zuerst an.")
        return

    stored_passwords = db.query(Password).filter(Password.user_id == user.id).all()
    db.close()

    if not stored_passwords:
        typer.echo("Keine Passwörter gefunden.")
        return

    table_data = []
    for stored_password in stored_passwords:
        decrypted_password = decrypt_password(stored_password.encrypted_password)
        table_data.append([stored_password.title, stored_password.username, decrypted_password])

    headers = ["Titel", "Benutzername", "Passwort"]
    table = tabulate(table_data, headers=headers, tablefmt="grid")
    typer.echo("Gespeicherte Passwörter:")
    typer.echo(table)


@app.command()
def delete_password(title: str):
    db = SessionLocal()
    user = get_logged_in_user(db)
    if user is None:
        typer.echo("Bitte melde dich zuerst an.")
        return

    password_to_delete = (
        db.query(Password)
        .filter(Password.title == title, Password.user_id == user.id)
        .first()
    )

    if password_to_delete is None:
        typer.echo("Kein Passwort mit diesem Titel gefunden.")
        db.close()
        return

    db.delete(password_to_delete)
    db.commit()
    db.close()

    typer.echo("Passwort erfolgreich gelöscht.")


@app.command()
def update_password(title: str, new_service_username: str, new_service_password: str):
    db = SessionLocal()
    user = get_logged_in_user(db)
    if user is None:
        typer.echo("Bitte melde dich zuerst an.")
        return

    password_to_update = (
        db.query(Password)
        .filter(Password.title == title, Password.user_id == user.id)
        .first()
    )

    if password_to_update is None:
        typer.echo("Kein Passwort mit diesem Titel gefunden.")
        db.close()
        return

    encrypted_new_password = encrypt_password(new_service_password)

    password_to_update.username = new_service_username
    password_to_update.encrypted_password = encrypted_new_password
    db.commit()
    db.close()

    typer.echo("Passwort erfolgreich aktualisiert.")
