function hello( name ) {
    return name == null ? "Hello!" : "Hello, " + name + "!";
}

module.exports.hello = hello;
