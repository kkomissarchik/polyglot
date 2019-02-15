# Hello Example - Bash

This is an implementation of the [Hello Example](../README.md) using Bash.

```
hello() {
    [ -z "$1" ] && echo "Hello!" || echo "Hello, $1!"
}

hello $1
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

* Bash - the scripting language and the runtime environment
