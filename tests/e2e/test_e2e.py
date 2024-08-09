import pytest

from click.testing import CliRunner

from my_tool.cli import command


@pytest.fixture
def mock_confuse(mocker):
    return mocker.patch("my_tool.cli.confuse")


@pytest.fixture
def runner():
    return CliRunner()


def test_say_hello_envvar(runner, monkeypatch):
    result = runner.invoke(command)
    assert "Hello, world!" in result.output
    assert result.exit_code == 0


def test_shout_hello_envvar(runner, monkeypatch):
    monkeypatch.setenv("MYTOOL_NAME", "TEST123ABC")
    result = runner.invoke(command, "--shout")
    assert "HELLO, WORLD!" in result.output
    assert result.exit_code == 0


def test_say_hello_envvar(runner, monkeypatch):
    monkeypatch.setenv("MYTOOL_NAME", "TEST123ABC")
    result = runner.invoke(command)
    assert "Hello, TEST123ABC!" in result.output
    assert result.exit_code == 0


def test_shout_hello_envvar(runner, monkeypatch):
    monkeypatch.setenv("MYTOOL_NAME", "TEST123ABC")
    result = runner.invoke(command, "--shout")
    assert "HELLO, TEST123ABC!" in result.output
    assert result.exit_code == 0
