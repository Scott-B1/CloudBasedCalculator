require 'test_helper'
#bin/rails test test/controllers/modulo_controller_test.rb
class ModuloControllerTest < ActionDispatch::IntegrationTest

  test "should return modulo success" do
    x = 4
    y = 2
    answer = x%y

    assert_equal 0, answer
  end

  test "should return negative modulo success" do
    x = -3
    y = 2
    answer = x%y

    assert_equal 1, answer
  end

end
