
import natural_whole_num


def test_check_natural_whole(mynum):
  testNumber = 6
  result = numCheck.NumberCheck(testNumber)
  
  assert result == -3, "The number is not whole number"
