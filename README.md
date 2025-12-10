# Brainless Embedding Service

A small FastAPI-based service that provides embeddings.

This repository contains a lightweight API for generating embeddings using a configurable model.

## Environment variables

- `DEBUG` — enable debug mode.
- `HF_TOKEN` — Hugging Face token.
- `MODEL_NAME` — name or path of the model to use for embeddings.
- `CACHE_FOLDER` — local folder path to cache model files.
- `API_KEY` — The API key is for naive authentication. The same key should be used by the client application. Any string

See `.env.example`

## Quick start

1. Set up the project using [uv](https://github.com/astral-sh/uv).
2. Create a `.env` file with any required variables (see above).
3. Use Makefile to run the application
