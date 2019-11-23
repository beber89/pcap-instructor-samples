

class QuerySyntaxError(Exception):
  pass

class QueryHandler:
  def __init__(self, orm):
    self.orm = orm
  def apply_query(self, query):
    command, column, _, table = query.lower().split()
    try:
      assert command == 'select' and table == 'employees'
      assert hasattr( self.orm.employee_list[0], column)
      self.result = list(map(lambda x: x.__getattribute__(column),  self.orm.employee_list))
    except AssertionError:
      raise QuerySyntaxError