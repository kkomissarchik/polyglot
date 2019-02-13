package polyglot.hello

fun hello( name: String? = null ): String {
    return if( name == null ) "Hello!" else "Hello, " + name + "!"
}

fun main( args: Array<String> ) {
    println( hello( if( args.size == 1 ) args[ 0 ] else null ) )
}
