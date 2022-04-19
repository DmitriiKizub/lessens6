from functions import salary, hello_who


# 1. Написать программу
# 2. отдельно проверить функцию
#print(hello_who('Max'))

# salary(2,10) == 20
#print(salary(2,10))

if salary(2,10) != 20:
    print('Ошибка')
if hello_who('Leo') != 'Hello,Leo':
    print('Ошибка')
if hello_who('Max') != 'Hello,Max':
    print('Ошибка')

print('ok')