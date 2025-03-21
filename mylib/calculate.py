#!/usr/bin/env python3


"""
This function is actually used to craete calculation function like add, subtract, multiply and divide.
This module will also be invoked by the test module to test the functionality of the functions.
This module will also be invoked as command line script using click.
"""

import click
def add(a, b):
    ""
    return a + b



def subtract(a, b): 
    return a - b    

def multiply(a, b):
    return a * b

def divide(a, b):        
    return a / b



# build a click group
@click.group()
def cli():
    """
    This is a simple calculator command line tool
    """
    pass

# build a click command
@cli.command("add")
@click.argument('a', type=float)
@click.argument('b', type=float)
def add(a, b):
    """
    This function adds two numbers
    """
    # invoke this function with coloured output from click
    click.echo(a + b)
    # add some more style 
    click.secho(f"{a} + {b} = {a+b}", fg="green")
    # no no more and more not satisfied
    click.secho(f"{a} + {b} = {a+b}", fg="green", bg="white")
    # no no more and more not satisfied
    click.secho(f"{a} + {b} = {a+b}", fg="green", bg="white", bold=True)
    # no no more and more not satisfied
    click.secho(f"{a} + {b} = {a+b}", fg="green", bg="white", bold=True, underline=True)
    # no no more and more not satisfied
    click.secho(f"{a} + {b} = {a+b}", fg="green", bg="white", bold=True, underline=True, blink=True)
    # no no more and more not satisfied
    click.secho(f"{a} + {b} = {a+b}", fg="green", bg="white", bold=True, underline=True, blink=True, reverse=True)
    # no no more and more not satisfied
    click.secho(f"{a} + {b} = {a+b}", fg="green", bg="white", bold=True, underline=True, blink=True, reverse=True, dim=True)
    # no no more and more not satisfied
    click.secho(f"{a} + {b} = {a+b}", fg="green", bg="white", bold=True, underline=True, blink=True, reverse=True, dim=True, italic=True)
    # no no more and more not satisfied
    click.secho(f"{a} + {b} = {a+b}", fg="green", bg="white", bold=True, underline=True, blink=True, reverse=True, dim=True, italic=True, strike=True)
    # no no more and more not satisfied
    click.secho(f"{a} + {b} = {a+b}", fg="green", bg="white", bold=True, underline=True, blink=True, reverse=True, dim=True, italic=True, strike=True, reset=True)
    # no no more and more not satisfied
    click.secho(f"{a} + {b} = {a+b}", fg="green", bg="white", bold=True, underline=True, blink=True, reverse=True, dim=True, italic=True, strike=True, reset=True, hidden=True)
    # no no more and more not satisfied
    click.secho(f"{a} + {b} = {a+b}", fg="green", bg="white", bold=True, underline=True, blink=True, reverse=True, dim=True, italic=True, strike=True, reset=True, hidden=True, bright=True)

# create virtual environment in github codespace
# python3 -m venv .venv
# source .venv/bin/activate
# pip install click
# pip freeze > requirements.txt
# git add .
# git commit -m "add click library"
# git push  






# build a click command
@cli.command("subtract")
@click.argument('a', type=float)
@click.argument('b', type=float)
def subtract(a, b):
    """
    This function subtracts two numbers
    """
    click.echo(a - b)

# build a click command
@cli.command("multiply")
@click.argument('a', type=float)
@click.argument('b', type=float)
def multiply(a, b):
    """
    This function multiplies two numbers
    """
    click.echo(a * b)

# build a click command
@cli.command("divide")
@click.argument('a', type=float)
@click.argument('b', type=float)
def divide(a, b):
    """
    This function divides two numbers
    """
    click.echo(a / b)

if __name__ == "__main__":
    cli()














# """
# Calculations library
# """


# def add(a, b):
#     return a + b


# def subtract(a, b):
#     return a - b


# def multiply(a, b):
#     return a * b


# def divide(a, b):
#     return a / b
