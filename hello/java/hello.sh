#!/bin/sh

mvn clean compile
echo
java -cp ./target/classes polyglot.hello.Greeter $1
echo
