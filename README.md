An example of how to structure and build a CLI tool in Python.

## Packaging and installation

This is really the main bit. The goal is to easily deploy a sytem-wide
application ready to run from the CLI or cron.

I think the best tool for this is `pipx`. You can configure it to install
to a system bin directory for maximum ease.

This uses a wheel built from `poetry build`:

```
# export PIPX_HOME=/opt/pipx
# export PIPX_BIN_DIR=/usr/local/bin/
# pipx install ./my_tool-1.0.0-py3-none-any.whl
% my-tool
Hello, world!
```

You can even install directly from github:

```
# export PIPX_HOME=/opt/pipx
# export PIPX_BIN_DIR=/usr/local/bin/
# pipx install git+https://github.com/i-hill/python-cli-tool.git
% my-tool
Hello, world!
```

## Configuration

This uses the [confuse](https://confuse.readthedocs.io/en/latest/index.html)
module for configuration. For example, you might supply the following
global configuration file:

```
% cat /etc/mytool/config.yaml 
name: Steve
% my-tool
Hello, Steve!
```

You can also use environment variables:

```
% MYTOOL_NAME="Bob" my-tool
Hello, Bob!
```

## Invocation

I always use the [click](https://click.palletsprojects.com/en/) project
for managing the CLI itself. You can easily build really complex apps this way -
mine is just an example!

```
% my-tool --help
Usage: my-tool [OPTIONS]

  Say hello to the nice people.

Options:
  -s, --shout  Speak more loudly.
  -h, --help   Show this message and exit.

% my-tool
Hello, world!
% my-tool --shout
HELLO, WORLD!
```

## Testing

Some example tests have been provided to give a flavour. Run them 
like this:

```
% poetry install
% poetry run pytest
```

These are also run from GitHub actions and a nice report is output.
