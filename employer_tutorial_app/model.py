class Employee:
  def __init__(self, **kwargs):
    ''' set attributes for employee according to kwargs ''' 
    for k, v in kwargs.items():
      self.__setattr__(k, v)
  def __repr__(self):
    if(hasattr(self, 'name') and hasattr(self, 'age') and hasattr(self, 'city')):
      return "name = %s, age = %d, city = %s"%( self.name, self.age, self.city)
    else:
      return None