#!/bin/sh

mvn clean compile
echo
java -cp ./target/classes polyglot.hello.java.Greeter $1
echo
