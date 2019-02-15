# Hello Example - Python

This is an implementation of the [Hello Example](../README.md) using Python.

```
def hello( name = None ):
    return "Hello!" if name is None else "Hello, " + name + "!"

def main( argv ):
    print( hello( argv[ 1 ] if len( argv ) == 2 else None ) )

if __name__ == "__main__": main( sys.argv )
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

* Python - the programming language and the runtime environment
* unittest - the test framework
