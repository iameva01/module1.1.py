calls = 0  # переменная для подсчета вызовов функций string_info & is_contains


def count_calls():  # будет использовать переменную calls и увеличивать ее на 1 при подсчете вызовов функций
    global calls
    calls += 1


def string_info(string): # принимает строку в качестве аргумента
    line1 = str(string) # преобразование ее в строку и сохраняет в переменной line1
    result = (len(line1), line1.upper(), line1.lower()) # кортеж, содержит длину строки, ее версию в верхнем и  нижнем регистрах
    count_calls() # счетчик вызовов
    return result # возвращает кортеж


def is_contains(string, list_to_search): # проверка наличия строки в списке
    string = str(string).lower() # преобразование в нижний регистр
    list_to_search = list(list_to_search) # и в строки
    count_calls() # счетчик вызовов
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result


print(string_info('Penguin'))
print(string_info('Rhinoceros'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
