#Якщо ви спробуєте змінити окремі символи рядка, як це було зроблено в попередньому кроці, ви отримаєте помилку TypeError, яка виникає, коли у коді використано об’єкт невідповідного типу.

text = 'Hello World'
text = 'Albatross'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift
