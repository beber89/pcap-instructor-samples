def ispalindrome(sentence):
  sentence = sentence.replace(" ", "")
  sentence = sentence.lower()
  reversed_sentence=list(reversed(sentence))  # reverse the sentence
  returnValue = True if sentence == "".join(reversed_sentence) else False
  return returnValue

x = input("please enter a statement\n")
print("is x a palindrome answer: ", ispalindrome(x))
# print(ispalindrome("Ten animals I slam in a net"))
