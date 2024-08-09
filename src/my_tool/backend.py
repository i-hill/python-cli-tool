"""
The business logic that knows how to actually get stuff done.
"""

from click import echo


def say_hello(to, shout=False):
    """Say hello to the nice user."""

    if shout:
        echo(f"HELLO, {to.upper()}!")
    else:
        echo(f"Hello, {to}!")
