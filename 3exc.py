import csv


def request_ship(file_name='space.txt'):
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
        name = input() # получаем на вход название корабля
        data = [i for i in reader] # заполняем данные из списка
        shipnames = [i['ShipName'] for i in data] #заполняем список с названиями кораблей
        dict_shipnames = {j['ShipName']: [j['direction'], j['planet']] for j in data} #заполняем словарь с значениями
        while name != 'stop': #обрабатываем стоп-фразу
            if name in shipnames: #проверяем есть ли такой корабль в списке названий
                direction = dict_shipnames[name][0]
                planet = dict_shipnames[name][1]
                print(f'Корабль {name} был отправлен с планеты: {planet} и его направление движения было: {direction}')
            else: #название не найдено
                print('error.. er.. ror..')
            
            name = input() #повторный ввод
            

request_ship(file_name = 'space.txt') #вызываем функцию
