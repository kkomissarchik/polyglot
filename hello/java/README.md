# Hello Example - Java

This is an implementation of the [Hello Example](../README.md) using Java.

```
public static String hello() {
    return hello( null );
}

public static String hello( final String name ) {
    return name == null ? "Hello!" : "Hello, " + name + "!";
}

public static void main( final String[] args ) {
    System.out.println( hello( args.length == 1 ? args[ 0 ] : null ) );
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

* Java - the programming language and the runtime environment
* JUnit - the test framework
* Maven - the build system
