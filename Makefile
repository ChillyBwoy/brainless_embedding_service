info: header

define header

Makefile for the API.
Usage:
  make dev        Run dev server
  make format     Format the code
  make help       Show this help
  make lint       Run linters
  make openapi    Generate openapi.json
  make preload    Preload models

endef
export header

include .env

.PHONY: help
help:
	@echo "$$header"

.PHONY: dev
dev:
	uv run fastapi dev app/main.py --port $(PORT)

.PHONY: format
format:
	uv run ruff format

.PHONY: lint
lint:
	uv run ruff check --no-fix
	uv run mypy --explicit-package-bases .
	uv run vulture --exclude ".venv/"  --min-confidence 100 .

.PHONY: openapi
openapi:
	uv run -m actions.openapi --app app.main:app --app-dir ./ --out ./openapi.json

.PHONY: preload
preload:
	uv run -m actions.preload


.DEFAULT_GOAL := help
