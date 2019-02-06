#!/bin/sh

python3 -m unittest -v tests.hello_test
echo
python3 -m hello $1
echo
