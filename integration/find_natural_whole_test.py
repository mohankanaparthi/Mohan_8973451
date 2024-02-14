
import natural_whole_num


def test_check_natural_whole(mynum):
  testNumber = 6
  result = check_number_type.NumberCheck(testNumber)
  
  assert result == -3, "The number is not whole number"
