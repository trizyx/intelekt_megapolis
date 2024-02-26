import csv


def sort(file_name='space.txt'):
    """Описание функции sort
    Функция выполняет сортировку за O(n^2) и выводит первые 10 кораблей

    Описание аргументов:
    file_name - имя исходного файла
    data - список с данными в таблице
    swap - переменная для проверки перемещения объекта в сортировке
    """
    with open(file=file_name, mode='r', encoding='utf8') as f: #открвыаем файл
        reader = csv.DictReader(f, delimiter='*') #считываем данные из файла
        data = [i for i in reader]
        swap = True
        while swap: 
            swap = False
            for i in range(len(data) - 1): #проходимся итеративно и сравниваем елементы
                for j in range(i, len(data) - 1):
                    if int(data[j]['ShipName'].split('-')[1]) > int(data[j + 1]['ShipName'].split('-')[1]): #сравниваем на то, какой больше
                        data[j], data[j + 1] = data[j + 1], data[j] #меняем местами
                        swap = True
    
        for i in range(10):
            print(data[i]['ShipName']) #возвращаем ответ


sort(file_name = 'space.txt') #вызываем функцию
