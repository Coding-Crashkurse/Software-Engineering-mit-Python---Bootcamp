import typer
from password_manager import main

app = typer.Typer()

@app.command()
def create_user(username: str, password: str):
    main.create_user(username, password)

@app.command()
def login(username: str, password: str):
    main.login(username, password)

@app.command()
def store_password(service: str, username: str, password: str):
    main.store_password(service, username, password)

@app.command()
def retrieve_password(service: str, username: str):
    password = main.retrieve_password(service, username)
    if password:
        typer.echo(f"Password for {username} on {service}: {password}")
    else:
        typer.echo(f"Could not find a password for {username} on {service}")


if __name__ == "__main__":
    app()
