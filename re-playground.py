# get numbers from a string
# get decimal numbers from a string
import re

inp = input("enter some text with numbers in it:\n")
pat = re.compile("\d+")
pat = re.compile("\d+(\.\d+)?")  # step 2
mat = pat.search(inp)

print(mat.group())
