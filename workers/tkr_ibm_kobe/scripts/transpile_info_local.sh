#!/bin/bash
set -euo pipefail

cp "$( dirname -- "${BASH_SOURCE[0]}" )"/../data/config.json $1
cp "$( dirname -- "${BASH_SOURCE[0]}" )"/../data/props.json $2

