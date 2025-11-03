#!/bin/bash
set -xeuo pipefail

source "$( dirname -- "${BASH_SOURCE[0]}" )"/backend_setup.sh ibm-kobe-dacc
"$( dirname -- "${BASH_SOURCE[0]}" )"/../build/transpile_info.o $1 $2

