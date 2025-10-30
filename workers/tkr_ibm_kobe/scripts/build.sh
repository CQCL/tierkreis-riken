#!/usr/bin/env bash
DIR=$( dirname "${BASH_SOURCE[0]}" )
source $DIR/backend_setup.sh ibm-kobe-dacc

uv run gcc $DIR/../tkr_sqcsub.cpp ${SQC_COMPILE_OPTIONS} $(uv run python -m pybind11 --includes)
# gcc -c -fPIC $DIR/../tkr_sqcsub.c -o $DIR/../build/tkr_sqcsub.o ${SQC_COMPILE_OPTIONS}
# gcc -shared -o $DIR/../build/tkr_sqcsub.so $DIR/../build/tkr_sqcsub.o ${SQC_COMPILE_OPTIONS}
