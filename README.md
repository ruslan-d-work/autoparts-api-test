# Autoparts API

A simple FastAPI-based microservice to store and manage car parts.

## Features

- Add a part (POST /parts/)
- Search parts (GET /parts/?search=)
- Delete parts (DELETE /parts/{id})

## Tech stack

- Python
- FastAPI
- SQLAlchemy
- SQLite

## Run locally

```bash
uvicorn main:app --reload
