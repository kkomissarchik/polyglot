#!/bin/bash

source ./greeter.sh

assertEquals() {
    if [[ $2 = $3 ]]
    then
        echo "$1 PASSED"
    else
        echo "$1 FAILED"
        echo "  expected: $3"
        echo "  actual: $2"
        exit 0
    fi
}

assertEquals "nameNotProvided" "$(hello)" "Hello!"
assertEquals "nameProvided" "$(hello Konstantin)" "Hello, Konstantin!"
