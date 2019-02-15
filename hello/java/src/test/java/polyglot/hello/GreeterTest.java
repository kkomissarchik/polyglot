package polyglot.hello;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public final class GreeterTest {

    @Test
    public void nameNotProvided1() {
        assertEquals( "Hello!", Greeter.hello() );
    }

    @Test
    public void nameNotProvided2() {
        assertEquals( "Hello!", Greeter.hello( null ) );
    }

    @Test
    public void nameProvided() {
        assertEquals( "Hello, Konstantin!", Greeter.hello( "Konstantin" ) );
    }

}
