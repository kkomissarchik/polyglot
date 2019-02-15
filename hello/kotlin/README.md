# Hello Example - Kotlin

These are several different implementations of the [Hello Example](../README.md) using Kotlin.

## Using if

```
fun hello( name: String? = null ): String {
    return if( name == null ) "Hello!" else "Hello, " + name + "!"
}
```

[Source Code](if/README.md)

## Using let

```
fun hello( name: String? = null ) = name?.let { "Hello, $it!" } ?: "Hello!"
```

[Source Code](let/README.md)

## Using when

```
fun hello( name: String? = null ) = when( name ) {
    null -> "Hello!"
    else -> "Hello, $name!"
}
```

[Source Code](when/README.md)
