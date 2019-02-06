import sys

def say( name ):
    return "Hello, " + name + "!"

def main( argv ):
    print( say( argv[ 1 ] if len( argv ) == 2 else "person" ) )

if __name__ == "__main__": main( sys.argv )
