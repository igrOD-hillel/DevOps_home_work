# Необходимо:
# С помощью модуля requests сделать запрос на https://baconipsum.com/api?type=meat-and-filler.
# Запросить минимум пять параграфов текста. Количество параграфов считывать в начале работы программы из
# стандартного ввода.
# Обратить вспять список строк в этом массиве. То есть сделать последнюю строку - первой(с индексом ноль),
# предпоследнюю - второй(с индексом 1) и т.д.
# Посчитать в ваших параграфах количество параграфов, в которых присутствует слово "Pancetta".
# Записать в файл следующую информацию: Ваше имя и дату вызова программы, цифру, которую мы посчитали в пункте 3 и
# обернутый вспять массив параграфов (параграфы объединить символами новой строки).
import datetime
import requests

count = int(input("Количество параграфов: "))
while 5 > count:
    count = int(input('Введенное кол-во параграфов меньше 5, введите минимум 5 параграфов: '))

data = requests.get(f"https://baconipsum.com/api/?type=meat-and-filler&paras={count}")
data_list = data.json()
data_log = datetime.date.today()
print(f'Скрипт запущен {data_log}')

data_list.reverse()
print(data_list)
name = 'Domushchei Ihor'
cnt = 0
new_list = []
for i in data_list:
    if 'Pancetta' in i or 'pancetta' in i:
        cnt += 1
    elif 'Pancetta,' in i or 'pancetta,' in i:
        cnt += 1
    elif "'Pancetta" in i or 'pancetta.' in i:
        cnt += 1
    else:
        continue
for i in data_list:
    new_list.append(f'{i}\n')
print(f"Найдено {cnt} слов 'Pancetta'")
out = [name, data_log, cnt, new_list]
with open('HW_08.txt', 'w') as file_data:
    for i in out:
        file_data.write(f"{i}\n")

