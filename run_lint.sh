#!/bin/sh

set -x
set -e

rm -rf pep8.log pyflakes.log

pep8 --max-line-length=81 pytd > pep8.log || true
pyflakes pytd > pyflakes.log || true
