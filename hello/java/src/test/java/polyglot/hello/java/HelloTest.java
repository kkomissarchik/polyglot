package polyglot.hello.java;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public final class HelloTest {

    @Test
    public void firstName() {
        assertEquals("Hello, Konstantin!", Hello.say("Konstantin"));
    }

}
