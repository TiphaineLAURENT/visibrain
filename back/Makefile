# Installation
~/.pyenv/bin/pyenv:
	sudo apt install curl bash
	curl -fsSL https://pyenv.run | bash

	# To be able to use pyenv outside of this setup
	# echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
	# echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
	# echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc

	# echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
	# echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
	# echo 'eval "$(pyenv init - bash)"' >> ~/.profile

	# exec "$SHELL"

.PHONY: poetry
poetry: ~/.pyenv/bin/pyenv
	sudo apt install pipx

	~/.pyenv/bin/pyenv install 3 --skip-existing

	pipx ensurepath
	pipx install poetry --python `~/.pyenv/bin/pyenv prefix 3`

.python-version:
	~/.pyenv/bin/pyenv local `~/.pyenv/bin/pyenv latest 3`

pyproject.toml:
	poetry config virtualenvs.in-project true
	poetry init --no-interaction --dev-dependency=ruff --dev-dependency=pyright

.venv:
	poetry install --no-root

init: .python-version poetry pyproject.toml .venv

# Project management
.PHONY: quality fix freeze
quality:
	-poetry run pyright
	-poetry run ruff format --diff
	-poetry run ruff check

fix:
	poetry run ruff format
	poetry run ruff check --fix

poetry.lock:
	poetry lock
freeze: poetry.lock

# If needed for some reason
.PHONY: clean
clean:
	rm -rf .ruff_cache poetry.lock .venv

run:
	poetry run
