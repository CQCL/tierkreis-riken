#!/usr/bin/env bash

echo ${SQC_COMPILE_OPTIONS}
uv run g++ -O3 -Wall -undefined dynamic_lookup -shared -std=c++11 -fPIC $(uv run python -m pybind11 --includes) tkr_sqcsub.cpp -o tkr_sqcsub$(uv run python -m pybind11 --extension-suffix) ${SQC_COMPILE_OPTIONS}