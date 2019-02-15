# Hello Example - Kotlin - if

This is an implementation of the [Hello Example](../../README.md) using Kotlin and its *if* expression.

```
fun hello( name: String? = null ): String {
    return if( name == null ) "Hello!" else "Hello, " + name + "!"
}
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

* Kotlin - the programming language and the runtime framework
* Java - the runtime environment
* JUnit - the test framework
* Gradle - the build system
