#!/bin/sh

rm -rf src
rm -rf target
rm -f pom.xml

cp -r ../../hello/java/src .
cp ../../hello/java/pom.xml .
