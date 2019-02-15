package polyglot.hello;

import java.util.Objects;

public final class Greeter {

    public static String hello() {
        return hello( null );
    }
    
    public static String hello( final String name ) {
        return name == null ? "Hello!" : "Hello, " + name + "!";
    }
    
    public static void main( final String[] args ) {
        System.out.println( hello( args.length == 1 ? args[ 0 ] : null ) );
    }

}
