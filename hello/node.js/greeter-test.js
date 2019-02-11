var assert = require( 'assert' );
var greeter = require( './greeter' );

describe( 'hello', function() {

    it( 'should greet with the provided name', function() {
        assert.equal( "Hello, Konstantin!", greeter.hello( "Konstantin" ) );
    });

});
