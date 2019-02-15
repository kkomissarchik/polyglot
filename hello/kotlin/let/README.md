# Hello Example - Kotlin (using let)

This is an implementation of the [Hello Example](../../README.md) using Kotlin and its *let* function.

```
fun hello( name: String? = null ) = name?.let { "Hello, $it!" } ?: "Hello!"
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
