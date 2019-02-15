#!/bin/sh

gradle clean compileScala

echo
scala -cp ./build/classes/scala/main polyglot.hello.Greeter $1
echo
