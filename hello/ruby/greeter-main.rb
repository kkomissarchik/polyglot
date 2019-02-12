require_relative "greeter"

puts hello( ARGV.length == 1 ? ARGV[ 0 ] : nil )
