#Оператори порівняння дозволяють порівнювати два об’єкти на основі їхніх значень.
#Ви можете використати оператор порівняння, розмістивши його між об’єктами, які потрібно порівняти.
#Вони повертають булеве (або логічне) значення: True або False, залежно від правдивості виразу.

#У Python є такі оператори порівняння:
#==	Дорівнює
#!=	Не дорівнює
#>	Більше
#<	Менше
#>=	Більше або дорівнює
#<=	Менше або дорівнює

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ' '

for char in text.lower():
    print(char == ' ')
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)