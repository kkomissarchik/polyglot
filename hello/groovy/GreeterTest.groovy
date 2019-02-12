class GreeterTest extends GroovyTestCase {

    void testNameNotProvided1() {
        assertEquals( "Hello!", Greeter.hello() )
    }

    void testNameNotProvided2() {
        assertEquals( "Hello!", Greeter.hello( null ) )
    }

    void testNameProvided() {
        assertEquals( "Hello, Konstantin!", Greeter.hello( "Konstantin" ) )
    }
   
}