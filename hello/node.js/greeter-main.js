var greeter = require( './greeter' );

console.log( greeter.hello( process.argv.length == 3 ? process.argv[ 2 ] : "person" ) );
