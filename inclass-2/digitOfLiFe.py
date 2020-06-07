
bd = input("Enter your birthday\n")
def digitOfLife(birthday):
  if(len(birthday) > 1):
    s = 0
    for char in birthday:
      s = s + int(char)
    return digitOfLife(str(s)) # 2
  else:
    return birthday


print("your digit of life is ", digitOfLife(bd))