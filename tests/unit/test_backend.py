import pytest

from my_tool.backend import say_hello


def test_say_hello(capsys):
    say_hello(to="world")
    captured = capsys.readouterr()
    assert "Hello, world!" in captured.out


def test_shout_hello(capsys):
    say_hello(to="world", shout=True)
    captured = capsys.readouterr()
    assert "HELLO, WORLD!" in captured.out
