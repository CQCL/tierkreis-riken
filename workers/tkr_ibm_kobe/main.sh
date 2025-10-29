#!/usr/bin/env bash
set -euo pipefail

source $(dirname "$0")/scripts/backend_setup.sh ibm-kobe-dacc

uv run main.py $1