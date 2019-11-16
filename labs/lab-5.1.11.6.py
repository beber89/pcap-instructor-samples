# Caesar cipher
text = input("Enter your message: ")
num = int(input("Number of shifts 1..25: "))
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    char = char.upper()

    # conversion takes place here
    code = (ord(char) - ord('A') + num)%(ord('Z')-ord('A')+1) + ord('A')
    cipher += chr(code)

print(cipher)