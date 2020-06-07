try:
  while True:
    text = input("Enter a sentence to be crypted\n")
    key = int(input("Enter the key between 1 to 25 "))
    cipher = ""
    for char in text.upper():
      if not char.isalpha():
        cipher = cipher + char
        continue
      code = (ord(char) - ord("A") + key) % (ord('Z') - ord('A') + 1)
      cipher = cipher + chr(code)

    print("Your coded text is \n", cipher)

except KeyboardInterrupt:
  print("You exited the program")


