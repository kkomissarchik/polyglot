#!/bin/sh

mvn clean test
echo
java -cp ./target/classes polyglot.hello.java.Hello $1
echo
