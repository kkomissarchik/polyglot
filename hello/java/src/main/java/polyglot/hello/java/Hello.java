package polyglot.hello.java;

import java.util.Objects;

public final class Hello {

    public static String say(final String name) {
        return "Hello, " + Objects.requireNonNull(name) + "!";
    }
    
    public static void main(final String[] args) {
        System.out.println(say(args.length == 1 ? args[0] : "person"));
    }

}
