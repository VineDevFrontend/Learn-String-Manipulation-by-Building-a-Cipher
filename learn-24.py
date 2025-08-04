#Якщо після останньої двокрапки не знайдено блоку з відступом, виконання коду припиняється та видається IndentationError. Цей код не показуватиме вивід, а натомість видасть IndentationError

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in text:
    print(i)
