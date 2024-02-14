import numCheck


def test_check_the_num():
  testNumber = 3
  result = numCheck.NumberCheck(testNumber)
  
  assert result == Positive, "The number is not a positive number"
