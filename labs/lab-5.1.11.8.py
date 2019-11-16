def areAnagrams(sentence1, sentence2):
  sentence1 = sentence1.lower().replace(" ",'')
  sentence2 = sentence2.lower().replace(" ",'')
  if sentence1 == '':
    return False
  for c in sentence1:
    index = sentence2.find(c)
    if index != -1:
      sentence2 = replaceStringAtIndex(sentence2, index, "")
    else:
      return False
  return sentence2 == ""

def replaceStringAtIndex(strng, i, c):
  strng = list(strng)
  strng[i]=c
  return "".join(strng)


print(areAnagrams("Listen", "Silent"))
print(areAnagrams("modern", "norman"))
