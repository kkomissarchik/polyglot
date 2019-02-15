#!/bin/sh

set -e

test() {
    echo
    echo "*************************************"
    echo "Testing $1"
    echo "*************************************"
    echo
    cd $1
    ./test.sh
    cd ..
}

for f in *; do
    if [ -d ${f} ]; then
        test "$f"
    fi
done
