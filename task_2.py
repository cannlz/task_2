import random


#Функция создания рандомного списка чисел
def gen_numbers():
    numbers_list = []
    for _ in range(3, 5):
        numbers_list.append(random.randint(2, 100))
    return numbers_list


#Функция поиска делителей
def find_divider():
    numbers_list = gen_numbers() #Получаем список чисел
    dividers_list = []

    for divider in range(1, 999): #Берём рандомный делитель
        for number in numbers_list: #Берём число из массива
            if number % divider == 0 and number > divider: #Проверка остатка от деления
                dividers_list.append(divider)

        if dividers_list.count(divider) != len(numbers_list) and dividers_list.count(divider) > 0: #Проверяем, подходит ли делитель ко всем числам в массиве(если нет - удаляем)
            dividers_list.remove(divider)
            
    dividers_list = list(set(dividers_list)) #Удаляем дубликаты

    return (f'Список чисел: {numbers_list}\nДелители: {dividers_list}')

print(find_divider())