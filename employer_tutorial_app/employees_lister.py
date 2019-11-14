# Specs: 
# Strings:
## Employess, list of dictionaries representing employee
## Employee can be entered using comma separated values
## Or can be entered one attribute at a time
# Modules:
## Put different input methods in two different functions
### repreenting input modes
## Might put different checks into different functions
### Even if implementation is one liner
### It becomes easier to understand logic from function name
## Port functions into different module
# Exceptions:
## ValueError when converting erroneous Employee age to integer
## KeyboardInterrupt Exception on the while loop

employees = []

while True:
  user_input = input("Please Enter Employee's name or 0 to Exit ... ")
  if user_input == '0':
    break
  elif user_input.isalpha():
    employees.append(user_input)
  else:
    print("Please Enter a Valid name !!!")

print(employees)
