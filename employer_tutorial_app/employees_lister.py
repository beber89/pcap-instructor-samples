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

from storage import ORM

def retreiveInput(user_input):
  [name, age] = user_input.split(',')
  return name, age

orm = ORM()
while True:
   try:
      user_input=input("Enter the name of employee, age and address or press 0 to enter a DB statement\n")

      user_input=user_input.split()
      user_input=''.join(user_input)
      user_input=user_input.split(",")
      name_var,age_var, city = user_input

      assert (name_var.isalpha()and age_var.isdigit())
      orm.write(name_var + ',' + age_var+ ', ' + city + '\n')
      orm.employee_list.append({'name':name_var,'age':age_var, 'address': city})

   except AssertionError:
      print("please enter valid values")
   except KeyboardInterrupt:
      print("good bye")
      break
print(orm.employee_list)
del orm
