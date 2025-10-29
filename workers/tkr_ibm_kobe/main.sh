#!/usr/bin/env bash
set -euo pipefail

DIR=$( dirname "${BASH_SOURCE[0]}" )

source $DIR/scripts/backend_setup.sh ibm-kobe-dacc

$DIR/.venv/bin/python $DIR/main.py $1