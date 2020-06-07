string = "hello workld,this is a string for a python playground ?? adsad"
# lab-5.1.9.18
def mysplit(strng):
  splits = []
  # loop
  index = strng.find(" ")
  while index != -1:
    # "world, this is a string for a python playground ?? adsad"
    splits.append(strng[0:index])
    strng = strng[(index+1):]
    # "adsad"
    index = strng.find(" ")
  #------
  splits.append(strng)
  return splits