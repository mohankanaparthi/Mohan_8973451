import numCheck


def test_check_the_num():
  testNumber = 6
  result = numCheck.NumberCheck(testNumber)
  
  assert result == -3, "The number is not negative"
