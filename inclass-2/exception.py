try:
  x = int(input("Please enter a positive number:\n"))
  assert x > 0  # AssertionError
except ValueError as msg:
  print(msg)
except AssertionError:
  print("Number is negative !!!")

print("Program done , out of while loop, output is ")