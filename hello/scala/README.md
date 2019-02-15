# Hello Example - Scala

This is an implementation of the [Hello Example](../README.md) using Scala.

```
def hello( name: String ): String = hello( Option( name ) )

def hello( name: Option[ String ] = None ) = name match {
    case Some( str ) => "Hello, " + str + "!"
    case None => "Hello!"
}

def main( args: Array[ String ] ) = {
    println( hello( args.headOption ) )
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

* Scala - the programming language and the runtime framework
* Java - the runtime environment
* ScalaTest - the test framework
* JUnit - the test framework
* Gradle - the build system
