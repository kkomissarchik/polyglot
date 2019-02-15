package polyglot.hello

fun hello( name: String? = null ): String {
    return if( name == null ) "Hello!" else "Hello, " + name + "!"
}

fun main( args: Array<String> ) {
    println( hello( args.firstOrNull() ) )
}
