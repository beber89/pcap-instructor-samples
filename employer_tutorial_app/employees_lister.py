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
from data_entry import DataEntry, DataEntryError

class UserPromptInputError(Exception):
   pass

def retreiveInput(user_input):
  [name, age] = user_input.split(',')
  return name, age

orm = ORM()
while True:
   try:
      user_input=input("Enter the name of employee, age and address or press 0 to enter a DB statement\n")
      if ',' in user_input:
         entry = DataEntry(orm, user_input)
         entry.apply_input()
      elif user_input == 0:
         # Create statement parser object
         pass
      else:
         raise UserPromptInputError
      

   except AssertionError:
      print("please enter valid values")
   except UserPromptInputError:
      print("please enter a valid choice")
   except KeyboardInterrupt:
      print("good bye")
      break
print(orm.employee_list)
del orm
