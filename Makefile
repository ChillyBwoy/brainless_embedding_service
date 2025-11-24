info: header

define header

Makefile for the API.
Usage:
  make help         show this help
  make lint         run linters
  make openapi      generate openapi.json
  make run          run the API
  make format       format the code

endef
export header

include .env

.PHONY: help
help:
	@echo "$$header"

.PHONY: run
run:
	fastapi dev main.py --port 8080


.PHONY: openapi
openapi:
	python -m actions.extract_openapi --app main:app --app-dir ./ --out ./openapi.json

.PHONY: lint
lint:
	ruff check --no-fix
	mypy --explicit-package-bases .
	vulture --exclude ".venv/"  --min-confidence 100 .

.PHONY: format
format:
	ruff format


.DEFAULT_GOAL := help
