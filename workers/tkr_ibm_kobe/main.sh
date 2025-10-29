#!/usr/bin/env bash
set -euo pipefail

DIR=$( dirname "${BASH_SOURCE[0]}" )
echo $DIR

source $DIR/scripts/backend_setup.sh ibm-kobe-dacc

echo "$DIR/.venv"
$DIR/.venv/bin/python $DIR/main.py $1
