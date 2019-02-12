#!/bin/bash

hello() {
    [ -z "$1" ] && echo "Hello!" || echo "Hello, $1!"
}
