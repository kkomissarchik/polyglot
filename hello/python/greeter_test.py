import greeter
import unittest

class HelloTest( unittest.TestCase ):

    def test_name_not_provided_1( self ):
        self.assertEqual( "Hello!", greeter.hello() )

    def test_name_not_provided_2( self ):
        self.assertEqual( "Hello!", greeter.hello( None ) )

    def test_name_provided( self ):
        self.assertEqual( "Hello, Konstantin!", greeter.hello( "Konstantin" ) )

if __name__ == '__main__':
    unittest.main()
