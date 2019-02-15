#!/bin/sh

gradle clean compileKotlin

echo
kotlin -cp ./build/classes/kotlin/main polyglot.hello.GreeterKt $1
echo
