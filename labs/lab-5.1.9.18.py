def mysplit(strng):
    strng = strng.strip()
    while strng.find("  ") != -1:
        strng = strng.replace("  ", " ")
    splits = []
    spcIndex = strng.find(" ")
    while spcIndex != -1:
        splits.append(strng[0:spcIndex])
        strng = strng[(spcIndex+1):]
        spcIndex = strng.find(" ")
    return splits + [strng] if strng != '' else splits
#
# put your code here
#


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

print(mysplit("Hello      world"))