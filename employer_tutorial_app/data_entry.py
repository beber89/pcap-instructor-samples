from model import Employee

class DataEntryError(Exception):
  pass

class DataEntry:
  def __init__(self, orm, user_input):
    self.orm = orm
    self.user_input = user_input
  
  def apply_input(self):
    try:
      user_input= self.user_input.split()
      user_input=''.join(user_input)
      user_input=user_input.split(",")
      name, age, city = user_input
      assert (name.isalpha()and age.isdigit())
      self.orm.write(name + ',' + age+ ', ' + city + '\n')
      self.orm.employee_list.append(Employee(name = name, age = int(age), city = city))
    except AssertionError:
      raise DataEntryError