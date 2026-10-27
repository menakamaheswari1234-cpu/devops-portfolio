#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
cd app
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest -q

cd ..

echo "Local validation passed."
