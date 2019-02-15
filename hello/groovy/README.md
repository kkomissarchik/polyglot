# Hello Example - Groovy

This is an implementation of the [Hello Example](../README.md) using Groovy.

```
def static hello( name = null ) {
    return name == null ? "Hello!" : "Hello, " + name + "!"
}

println hello( args.length == 1 ? args[ 0 ] : null )
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

* Groovy - the programming language and the runtime environment
