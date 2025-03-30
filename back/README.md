# Python template

A template for python projects, including basic setup and depencies management

## Usage

All commands are to be executed with make like
```sh
make <command>
```

### Setup

This project depends on make and apt and will fail otherwise.

- **init**:
This will install curl, bash, pipx, pyenv and poetry.
But will also install the new project with dev tools.


### Project management

- **quality**:
Will run dev tools to analyse code and format code without modifying any files.

- **fix**:
Will run dev tools to analyse code and format code files.

- **freeze**:
Freezes currently installed dependencies


### Miscellaneous

- **clean**:
Removes generated files like .venv, poetry-lock and tools cache
