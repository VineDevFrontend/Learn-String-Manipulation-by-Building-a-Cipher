text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)
#можна використати оператор додавання +, так само як і в математичному додаванні.
shifted = alphabet[index + shift]
print(shifted)