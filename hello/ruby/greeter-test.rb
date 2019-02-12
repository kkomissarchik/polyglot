require_relative "greeter"
require "test/unit"
 
class GreeterTest < Test::Unit::TestCase
 
  def test_name_not_provided_1
    assert_equal( "Hello!", hello() )
  end
 
  def test_name_not_provided_2
    assert_equal( "Hello!", hello( nil ) )
  end
 
  def test_name_provided
    assert_equal( "Hello, Konstantin!", hello( "Konstantin" ) )
  end
 
end
