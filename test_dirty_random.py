from dirty_functions import random_famous
import os
def test_random_famous():
    # Кол-во возрващаемых ээлементов списка
    FAMOUS = ('Pushkin', 'Max', 'Leo', 'Kate')
    assert len(random_famous(FAMOUS, 2)) == 2

    # что вернулось то что есть в исходном списке а не левые элементы
    # assert lambda x: x in len(random_famous(('Pushkin','Max','Leo','Kate'),2))
    for i in random_famous(FAMOUS, 2):
        assert i in (FAMOUS)

    # 2 Тип строка данных, тип строки
    first_person = random_famous(FAMOUS, 2)[0]
    assert isinstance(first_person, str)

    first_person = random_famous(({'Leo': 30}, {'Max': 20}), 2)[0]
    #assert isinstance(first_person, str)

    # Как проверить что они рандом
    result = []
    for i in range(800):
        person = random_famous(FAMOUS, 1)[0]
        result.append(person)
    assert len(set(result)) > 1


def test_mkdir():
    '''
    Тест для функции с побочным эффектом
    :param name:
    :return:
    '''
    os.mkdir('folder_mk')
    assert 'folder_mk' in os.listdir()
    os.rmdir('folder_mk')