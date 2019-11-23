import os
from model import Employee

class ORM:
  def __init__ (self):
    self.load("employees.txt")

  def __del__ (self):
    print("Object ORM is leaving...\nGood Bye !!!")
    self.fo.close()

  def write(self, text):
    self.fo.write(text)

  def load(self, filename):
      lst = []
      self.fo = open(filename, "a+")
      self.fo.seek(0, os.SEEK_SET)
      line = self.fo.readline()
      while line != '':
          name, age, city = line.split(',')
          lst.append(Employee(name = name,age = int(age), city = city[:-1]))
          line = self.fo.readline()
      self.fo.seek(0, os.SEEK_END)
      self.employee_list = lst
  def close(self):
    self.fo.close()