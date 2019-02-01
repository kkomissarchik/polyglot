package polyglot.hello.java;

import java.util.Objects;

public final class Hello {

    public static String say(final String name) {
        return "Hello, " + Objects.requireNonNull(name) + "!";
    }

}
