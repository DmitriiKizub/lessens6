def hello_who(name):
    """

    :param name:
    :return:
    """
    return f'Hello, {name}'

def salary(hours, salary_by_hour):
    #Рассчет ЗП сотрудника
    # hour: кол-во часов
    # salary_by_hour: Зарплата за час
    # return: итоговая стоимость
    k = 1
    return hours*salary_by_hour*k