import csv


def replace_null_cord(file_name='space.txt', output_file_name='space_new.txt'):
    """Описание функции replace_null_cor
    Функция заменяет нулевые значения в координатах корабля(file_name), сохраняет файл 
    с измененными координатами(output_file_name) и выводит все корабли, 
    где последний элемент их кода равен “V” в формате <ShipName> - (<x>, <y>)

    Описание аргументов:
    file_name - имя исходного файла
    output_file_name - имя файла для записи
    out_data - список для хранения всех строк исходной таблицы с измененными нулевыми координатами
    column_with_nulls - столбец с нулевыми значениями
    n – первая цифра в номере корабля, m – вторая цифра в номере корабля, t - кол-во букв в родной  планете корабля
    xd, yd - координаты вектора направления

    """
    file_name = 'space.txt'
    output_file_name = 'space_new.txt'
    out_data = []

    with open(file=file_name, mode='r', encoding='utf8') as f: #открвыаем файл
        reader = csv.DictReader(f, delimiter='*') #считываем данные из файла
        column_with_nulls = 'coord_place'
        for row in reader: #итеративно проходимся по всем данным
            if '0 0' in row[column_with_nulls]: #заполняем значения для каждой строки если в ее координаты равны 0 0
                n = int(row['ShipName'].split('-')[1][0])
                m = int(row['ShipName'].split('-')[1][1])
                xd = int(row['direction'].split()[0])
                yd = int(row['direction'].split()[1])
                t = len(row['planet'])
                # блок с условиями
                if n > 5:
                    row[column_with_nulls] = str(n + xd)

                if n <= 5:
                    row[column_with_nulls] = str(-(n + xd) * 4 + t)
            
                if m > 3:
                    row[column_with_nulls] += f' {m + t + yd}'
            
                if m <= 3:
                    row[column_with_nulls] += f' {-(n + yd) * m}'

            out_data.append(row) #дополняем список с выходными данными

    with open(file=output_file_name, mode='w', encoding='utf8') as out: #открываем файл на запись
        writer = csv.DictWriter(f=out, delimiter='*', fieldnames=list(out_data[0].keys())) 
        writer.writeheader() #записываем заголовки
        writer.writerows(out_data) #записываем данные

    print('ANSWER-----------')
    for i in out_data:#итеративно проходимся по списку данных
        if i['ShipName'][3] == 'V':#если последний символ в коде = V то выводим ответ
            x = i['direction'].split()[0]
            y = i['direction'].split()[1]
            print(f"{i['ShipName']} - ({x}, {y})")


replace_null_cord(file_name = 'space.txt',
                  output_file_name = 'space_new.txt') #вызываем функцию
