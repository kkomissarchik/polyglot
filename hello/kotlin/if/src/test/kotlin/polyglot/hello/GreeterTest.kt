package polyglot.hello

import kotlin.test.assertEquals
import org.junit.Test

class GreeterTest {

    @Test fun nameNotProvided1() {
        assertEquals( "Hello!", hello() )
    }

    @Test fun nameNotProvided2() {
        assertEquals( "Hello!", hello( null ) )
    }

    @Test fun nameProvided() {
        assertEquals( "Hello, Konstantin!", hello( "Konstantin" ) )
    }

}
