#!/usr/bin/env bash

source ./scripts/backend_setup.sh ibm-kobe-dacc

uv run main.py $1