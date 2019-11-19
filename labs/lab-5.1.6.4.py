def readint(prompt, min, max):
    while True:
        try:
            val = int(input(prompt))
            assert val >= min and val <= max
            return val
        except ValueError:
            print("Error: wrong input")
            continue
        except AssertionError:
            print(" the value is not within permitted range ("+str(min)+".."+str(max)+")")
            continue
#
# put your code here
#

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
