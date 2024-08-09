An example of how to structure and build a CLI tool in Python.

## Packaging and installation

This is really the main bit. The goal is to easily deploy a sytem-wide
application ready to run from the CLI or cron.

I think the best tool for this is `pipx`. You can configure it to install
to a system bin directory for maximum ease:

```
% export PIPX_HOME=/opt/pipx
% export PIPX_BIN_DIR=/usr/local/bin/
% pipx install ./my_tool-1.0.0-py3-none-any.whl
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

## Testing

Some example tests have been provided to give a flavour. Run them 
like this:

```
% poetry install
% poetry run pytest
```

Ideally you'd run this from your CI pipeline with protections to
ensure a clean environment (for example, running them in a disposable
container).
