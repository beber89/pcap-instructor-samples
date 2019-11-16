def isPalindrome(sentence):
  if sentence.replace(' ','') == '':
    return False
  rev = "".join(list(reversed(sentence.lower())))
  return rev.replace(" ", '') == sentence.lower().replace(" ", '')

print(isPalindrome("Ten animals I slam in a net"))
print(isPalindrome("Eleven animals I slam in a net"))