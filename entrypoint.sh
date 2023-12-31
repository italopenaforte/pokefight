#!/bin/bash
set -e

uvicorn src.__main__:app --reload --port=5000 --host=0.0.0.0
