package polyglot.hello

object Greeter {

    def hello( name: String ): String = hello( Option( name ) )

    def hello( name: Option[ String ] = None ) = name match {
        case Some( str ) => "Hello, " + str + "!"
        case None => "Hello!"
    }

    def main( args: Array[ String ] ) = {
        println( hello( args.headOption ) )
    }
    
}
