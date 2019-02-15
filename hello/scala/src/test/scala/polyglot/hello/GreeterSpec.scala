package polyglot.hello

import org.junit.runner.RunWith
import org.scalatest.FlatSpec
import org.scalatest.junit.JUnitRunner

@RunWith( classOf[ JUnitRunner ] )
class GreeterSpec extends FlatSpec {

    "Greeter" should "greet an unnamed party generically (1)" in {
        assert( Greeter.hello() == "Hello!" )
    }

    it should "greet an unnamed party generically (2)" in {
        assert( Greeter.hello( null.asInstanceOf[ String ] ) == "Hello!" )
    }

    it should "greet an unnamed party generically (3)" in {
        assert( Greeter.hello( None ) == "Hello!" )
    }

    it should "greet a named party with the provided name" in {
        assert( Greeter.hello( "Konstantin" ) == "Hello, Konstantin!" )
    }

}
