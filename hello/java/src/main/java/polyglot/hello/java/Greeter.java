package polyglot.hello.java;

import java.util.Objects;

public final class Greeter {

    public static String hello( final String name ) {
        return "Hello, " + Objects.requireNonNull( name ) + "!";
    }
    
    public static void main( final String[] args ) {
        System.out.println( hello( args.length == 1 ? args[ 0 ] : "person" ) );
    }

}
