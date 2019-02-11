package polyglot.hello.java;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public final class GreeterTest {

    @Test
    public void firstName() {
        assertEquals( "Hello, Konstantin!", Greeter.hello( "Konstantin" ) );
    }

}
