# Hello Example

A simple function with a command line interface and unit tests.

## Requirements

* Provide a function that takes an optional name parameter and returns either "Hello!" or "Hello, [name]!",
  dependent on whether a name is provided
* Provide a way to invoke this function from the command line
* Provide unit tests

## Bash

```
hello() {
    [ -z "$1" ] && echo "Hello!" || echo "Hello, $1!"
}

hello $1
```

[Source Code](bash/README.md)

## Groovy

```
def static hello( name = null ) {
    return name == null ? "Hello!" : "Hello, " + name + "!"
}

println hello( args.length == 1 ? args[ 0 ] : null )
```

[Source Code](groovy/README.md)

## Java

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

[Source Code](java/README.md)

## Kotlin (using if)

```
fun hello( name: String? = null ): String {
    return if( name == null ) "Hello!" else "Hello, " + name + "!"
}

fun main( args: Array<String> ) {
    println( hello( args.firstOrNull() ) )
}
```

[Source Code](kotlin/if/README.md)

## Kotlin (using let)

```
fun hello( name: String? = null ) = name?.let { "Hello, $it!" } ?: "Hello!"

fun main( args: Array<String> ) {
    println( hello( args.firstOrNull() ) )
}
```

[Source Code](kotlin/let/README.md)

## Kotlin (using when)

```
fun hello( name: String? = null ) = when( name ) {
    null -> "Hello!"
    else -> "Hello, $name!"
}

fun main( args: Array<String> ) {
    println( hello( args.firstOrNull() ) )
}
```

[Source Code](kotlin/when/README.md)

## Node.js

```
function hello( name ) {
    return name == null ? "Hello!" : "Hello, " + name + "!";
}

console.log( hello( process.argv.length == 3 ? process.argv[ 2 ] : null ) );
```

[Source Code](node.js/README.md)

## Python

```
def hello( name = None ):
    return "Hello!" if name is None else "Hello, " + name + "!"

def main( argv ):
    print( hello( argv[ 1 ] if len( argv ) == 2 else None ) )

if __name__ == "__main__": main( sys.argv )
```

[Source Code](python/README.md)

## Ruby

```
def hello( name = nil )
   return name ? "Hello, " + name + "!" : "Hello!"
end

puts hello( ARGV.length == 1 ? ARGV[ 0 ] : nil )
```

[Source Code](ruby/README.md)

## Scala

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

[Source Code](scala/README.md)

