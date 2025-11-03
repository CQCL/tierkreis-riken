#!/bin/bash
set -euo pipefail

source "$( dirname -- "${BASH_SOURCE[0]}" )"/backend_setup.sh ibm-kobe-dacc
"$( dirname -- "${BASH_SOURCE[0]}" )"/../build/submit.o $1 $2 $3 $4
