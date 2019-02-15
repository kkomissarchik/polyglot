#!/bin/sh

set -e

hello() {
    echo
    echo "*************************************"
    echo "Hello $1"
    echo "*************************************"
    echo
    cd $1
    ./hello.sh $2
    cd ..
}

for f in *; do
    if [ -d ${f} ]; then
        hello "$f" $1
    fi
done
