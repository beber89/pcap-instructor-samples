
employees = []

while True:
  user_input = input("Please Enter Employee's name or 0 to Exit ... ")
  if user_input == '0':
    break
  else:
    employees.append(user_input)

print(employees)
