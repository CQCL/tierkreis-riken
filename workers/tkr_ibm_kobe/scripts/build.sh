#!/bin/bash
set -xeuo pipefail

source "$( dirname -- "${BASH_SOURCE[0]}" )"/backend_setup.sh ibm-kobe-dacc
gcc "$( dirname -- "${BASH_SOURCE[0]}" )"/../src/transpile_info.c -o build/transpile_info.o ${SQC_COMPILE_OPTIONS}
gcc "$( dirname -- "${BASH_SOURCE[0]}" )"/../src/submit.c -o build/submit.o ${SQC_COMPILE_OPTIONS} 

