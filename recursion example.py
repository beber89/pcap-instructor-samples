def mydigit(p):
    s = 0
    for x in p:
        s += int(x)
    if s < 10:
        return s
    else:
        return mydigit(str(s))

user_input = input("birthday \n")
print(mydigit(user_input))
