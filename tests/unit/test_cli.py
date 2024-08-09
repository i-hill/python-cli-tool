import pytest

from click.testing import CliRunner

from my_tool.cli import command


@pytest.fixture
def mock_say_hello(mocker):
    return mocker.patch("my_tool.cli.say_hello")

@pytest.fixture
def mock_confuse(mocker):
    return mocker.patch("my_tool.cli.confuse")
    
@pytest.fixture
def runner():
    return CliRunner()


def test_say_hello(runner, mock_say_hello):
    result = runner.invoke(command)
    mock_say_hello.assert_called_with(to="world", shout=False)
    assert result.exit_code == 0


def test_shout_hello(runner, mock_say_hello):
    result = runner.invoke(command, "--shout")
    mock_say_hello.assert_called_with(to="world", shout=True)
    assert result.exit_code == 0


def test_say_hello_custom_name(runner, mock_say_hello, mock_confuse):
    mock_confuse.Configuration.return_value.__getitem__.return_value.get.return_value = "TEST321XYZ"
    result = runner.invoke(command)
    mock_say_hello.assert_called_with(to="TEST321XYZ", shout=False)
    assert result.exit_code == 0

