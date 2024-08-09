"""
The main application CLI."
"""

import click
import confuse

from .backend import say_hello


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"], color=True)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("--shout", "-s", is_flag=True, help="Speak more loudly.")
def command(shout):
    """Say hello to the nice people."""

    config = confuse.Configuration("mytool", __name__)
    config.set_env()
    name = config["name"].get(str)
    say_hello(to=name, shout=shout)
