#!/bin/bash

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# Run backend server
uvicorn backend.app:app --reload
