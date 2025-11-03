#!/bin/bash
set -euo pipefail

for arg in "$@"; do
  shift
  if [[ "$arg" == "--ofile" ]]; then
    break;
  fi;
done

cp "$( dirname -- "${BASH_SOURCE[0]}" )"/../data/result.json $1
