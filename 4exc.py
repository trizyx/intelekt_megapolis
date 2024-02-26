import csv


def generate_password(file_name='space.txt', output_file_name='space_uniq_password.csv'):
    """Описание функции sort
    Функция выводит по названию корабля название родной планеты и направление движения в формате:
    Корабль <ShipName> был отправлен с планеты: <planet> и его направление движения было: <direction>
    
    Остановка работы функции происходит в случае ввода stop

    Описание аргументов:
    file_name - имя исходного файла
    data - список с данными в таблице
    shipnames - список названий кораблей
    dict_shipnames - словарь в формате ключ: название корабля; значение - направление и планета
    name - получаемое на вход название корабля
    direction - направление движения корабля
    planet - исходная планета корабля
    """
    with open(file=file_name, mode='r', encoding='utf8') as f: #открвыаем файл
        reader = csv.DictReader(f, delimiter='*') #считываем данные из файла
        data = [i for i in reader] # заполняем данные из списка
        passwords = [] # список паролей
        for i in data:
            print(i)
            password = i['planet'][-3:] + i['ShipName'].split('-')[0][1:3][::-1] + i['planet'][:3][::-1] # создаем пароль
            password = password.upper()
            passwords.append(password)

    with open(file=output_file_name, mode='w', encoding='utf8') as out: #открываем файл на запись
        writer = csv.DictWriter(f=out, delimiter='*', fieldnames='password') 
        writer.writeheader() #записываем заголовки
        writer.writerows(passwords) #записываем данные
        

generate_password(file_name = 'space.txt', output_file_name='space_uniq_password.csv') #вызываем функцию
