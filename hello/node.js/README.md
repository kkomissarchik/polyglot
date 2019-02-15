# Hello Example - Node.js

This is an implementation of the [Hello Example](../README.md) using JavaScript and Node.js platform.

```
function hello( name ) {
    return name == null ? "Hello!" : "Hello, " + name + "!";
}

console.log( hello( process.argv.length == 3 ? process.argv[ 2 ] : null ) );
```

## Usage

Invoke the hello function like so:

```
./hello.sh
```

or

```
./hello.sh [name]
```

Run the tests like so:

```
./test.sh
```

## Technologies

* JavaScript - the programming language
* Mocha - the test framework
* Node.js - the runtime environment
