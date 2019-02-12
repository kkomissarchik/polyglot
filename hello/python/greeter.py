import sys

def hello( name = None ):
    return "Hello!" if name is None else "Hello, " + name + "!"

def main( argv ):
    print( hello( argv[ 1 ] if len( argv ) == 2 else None ) )

if __name__ == "__main__": main( sys.argv )
