import  random
import os
def random_famous(famous, count = 2):
    '''

    :param famous: Список людей
    :param count: Кол-во
    :return: Возвращает случайных людей
    '''
    return random.sample(famous,count)
