# Project Polyglot

Project Polyglot is a learning resource for comparing and contrasting implementations of the same requirements
using different programming languages and technical stacks.

This project is similar to other programming chrestomathy efforts, such [Rosetta Code](http://www.rosettacode.org),
but with emphasis on runnable projects rather than code snippets.

Why polyglot? A polyglot is someone who can speak or use several different languages.

## Hello Example

A simple function with a command line interface and unit tests.

* Requirements
    * Provide a function that takes a name and returns a string "Hello, [name]!"
    * Provide a way to invoke this function from the command line
    * Provide unit tests
* Implementations
    * [Bash](hello/bash/README.md)
    * [Java](hello/java/README.md)
    * [Node.js](hello/node.js/README.md)
    * [Python](hello/python/README.md)

## Build Example

A build system that compiles the source code and runs the unit tests.

* Requirements
    * Provide a facility to compile the source code
    * Provide a facility to run the unit tests
* Implementations
    * [Ant with Ivy](build/ant-ivy/README.md)
    * [Gradle](build/gradle/README.md)
    * [Maven](build/maven/README.md)
