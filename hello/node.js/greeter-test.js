var assert = require( 'assert' );
var greeter = require( './greeter' );

describe( 'hello', function() {

    it( 'should greet an unnamed party correctly (1)', function() {
        assert.equal( "Hello!", greeter.hello() );
    });

    it( 'should greet an unnamed party correctly (2)', function() {
        assert.equal( "Hello!", greeter.hello( null ) );
    });

    it( 'should greet a named party with the provided name', function() {
        assert.equal( "Hello, Konstantin!", greeter.hello( "Konstantin" ) );
    });

});
