#!/usr/bin/env bash

cmake -S . -B build -DPython_EXECUTABLE=./.venv/bin/python -DPYTHON_INCLUDE_DIR=$(python -c "import sysconfig; print(sysconfig.get_path('include'))")  \
    -DPYTHON_LIBRARY=$(python -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")
cmake --build build