package polyglot.hello

fun hello( name: String? = null ) = when( name ) {
    null -> "Hello!"
    else -> "Hello, $name!"
}

fun main( args: Array<String> ) {
    println( hello( args.firstOrNull() ) )
}
