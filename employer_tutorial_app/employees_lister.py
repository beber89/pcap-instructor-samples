# Specs: 
# Strings:
## [X] Employess, list of dictionaries representing employee
## [X] Employee can be entered using comma separated values
## Or can be entered one attribute at a time
# Modules:
## Put different input methods in two different functions
### representing input modes
## Might put different checks into different functions
### Even if implementation is one liner
### It becomes easier to understand logic from function name
## Port functions into different module
# Exceptions:
## ValueError when converting erroneous Employee age to integer
## KeyboardInterrupt Exception on the while loop

employees = []

while True:
  user_input = input(\
    "Please Enter Employee's name and age separated by comma\n"\
    +"or enter 0 to Exit ...\n")
  if user_input == '0':
    break
  elif ',' not in user_input:
    print('please enter name and age separated by comma')
    continue
  else:
    name, age = user_input.split(',')
    if not name.isalpha() or not age.isdigit():
      print("Please Enter a Valid name and age !!!")
      continue
    employees.append({'name': name, 'age': age})
      

print(employees)
