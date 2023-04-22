# import typer
#
# app = typer.Typer()
#
#
# @app.command()
# def hello(name: str):
#     print(f"Hello {name}")
#
#
# @app.command()
# def goodbye(name: str, formal: bool = False)  :
#     if formal:
#         print(f"Bye Mr. {name}!")
#     else:
#         print(f"Bye {name}!")
#
#
# if __name__ == "__main__":
#     app()

import typer

app = typer.Typer()

@app.command()
def hello(name: str = typer.Argument(..., help="Name of the person to greet")):
    print(f"Hello {name}")

@app.command()
def goodbye(
    # name: str = typer.Argument(..., help="Name of the person to say goodbye to"),
    name: str = typer.Option(..., prompt=True, help="Name of the person to say goodbye to"),
    formal: bool = typer.Option(False, "--f", help="Use a formal goodbye"),
    age: int = typer.Option(None, help="Age of the person to say goodbye to"),
):
    if formal:
        message = f"Goodbye, Mr. {name}!"
    else:
        message = f"Goodbye, {name}!"

    if age is not None:
        message += f" Best wishes on your {age} years!"

    print(message)

import re

def validate_password(value: str) -> str:
    if len(value) < 8:
        typer.echo("Das Passwort muss mindestens 8 Zeichen lang sein.", err=True)
        raise typer.Exit()

    if not re.search(r'\d', value):
        typer.echo("Das Passwort muss mindestens eine Zahl enthalten.", err=True)
        raise typer.Exit()

    if not re.search(r'[A-Z]', value):
        typer.echo("Das Passwort muss mindestens einen Großbuchstaben enthalten.", err=True)
        raise typer.Exit()

    return value


@app.command()

def set_password(
        password: str = typer.Option(
            ..., prompt=True, confirmation_prompt=True, hide_input=True, callback=validate_password
        )):
    print(password)

if __name__ == "__main__":
    app()
