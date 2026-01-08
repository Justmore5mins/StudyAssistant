.PHONY: setup venv markitdown gemini

VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

setup: venv markitdown gemini final

venv:
	python3.13 -m venv $(VENV)

markitdown:
	@if [ ! -d markitdown ]; then \
		git clone https://github.com/microsoft/markitdown.git; \
	fi
	$(PIP) install -e 'markitdown/packages/markitdown[all]'

gemini:
	command -v brew >/dev/null 2>&1 || { echo "Homebrew not installed"; exit 1; }
	brew install gemini

final:
	echo "Everything is ok"