# Hello Example - Ruby

This is an implementation of the [Hello Example](../README.md) using Ruby.

```
def hello( name = nil )
   return name ? "Hello, " + name + "!" : "Hello!"
end

puts hello( ARGV.length == 1 ? ARGV[ 0 ] : nil )
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

* Ruby - the programming language and the runtime environment
* Test::Unit - the test framework
