def digitOfLife(dateAsStr):
  if(len(dateAsStr) > 1):
    s = 0
    for num in dateAsStr:
      s += int(num)
    return digitOfLife(str(s))
  return dateAsStr

print(digitOfLife("19891110"))
print(digitOfLife("19891011"))
print(digitOfLife("20001001"))
print(digitOfLife("20180909"))

# implementation without recursion
def digitOfLife2(dateAsStr):
  s = 0
  while len(str(s)) > 1:
    for num in dateAsStr:
      s += int(num)
  return s

print(digitOfLife("19891110"))
print(digitOfLife("19891011"))
print(digitOfLife("20001001"))
print(digitOfLife("20180909"))