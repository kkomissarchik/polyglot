package polyglot.hello

fun hello( name: String? = null ) = name?.let { "Hello, $it!" } ?: "Hello!"

fun main( args: Array<String> ) {
    println( hello( args.firstOrNull() ) )
}
