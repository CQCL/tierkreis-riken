#!/bin/bash
set -xeuo pipefail

cp "$( dirname -- "${BASH_SOURCE[0]}" )"/../data/config.json $1
cp "$( dirname -- "${BASH_SOURCE[0]}" )"/../data/props.json $2

