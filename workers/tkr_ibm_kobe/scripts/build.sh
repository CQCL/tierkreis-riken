#!/usr/bin/env bash

source ./scripts/backend_setup.sh ibm-kobe-dacc

gcc -c -fPIC ./src/tkr_sqcsub.c -o ./build/tkr_sqcsub.o ${SQC_COMPILE_OPTIONS}
gcc -shared -o ./build/tkr_sqcsub.so ./build/tkr_sqcsub.o ${SQC_COMPILE_OPTIONS}
