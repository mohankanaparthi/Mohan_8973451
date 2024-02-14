import numCheck


def check_the_num(mynum):
  testNumber = 6
  result = numCheck.NumberCheck(testNumber)
  
  assert result == -3, "The number is not negative"
