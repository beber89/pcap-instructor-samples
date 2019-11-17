# Specs: 
# [X] Strings:
## [X] Employess, list of dictionaries representing employee
## [X] Employee can be entered using comma separated values
## [ ] Parser: parse a filter instruction entered by user
## Or can be entered one attribute at a time
# Modules:
## [ ] Put different input methods in two different functions
### representing input modes
## [ ] Put employees array in different module
## [ ] Might put different checks into different functions
### Even if implementation is one liner
### It becomes easier to understand logic from function name
## [ ] Port other functions into different module
# [X] Exceptions:
## [X] ValueError when converting erroneous Employee age to integer
## [X] KeyboardInterrupt Exception on the while loop
# Generators:
## In DataStore Module implement a filter method as generator

employees = []

def retreiveInput(user_input):
  [name, age] = user_input.split(',')
  return name, age

try:
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
      name, age = retreiveInput(user_input)
      if not name.isalpha():
        print("Please Enter a Valid name !!!")
        continue
      try:
        employees.append({'name': name, 'age': int(age)})
      except ValueError:
        print("Please Enter a Valid age !!!\n")
        continue
except KeyboardInterrupt:
  print("User forcibly exited the application")
finally:
  print(employees)



