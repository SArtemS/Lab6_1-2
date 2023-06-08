from typing import List
from mathstats import MathStats

FILE = 'Retail.csv'
FILE2 = 'MarketingSpend.csv'


def main():
    # запускающая функция
    data = read_data(FILE)
    print(f'Всего уникальных инвойсов (invoices): {count_invoice(data)}') # 16522
    print(f'Число уникальных значений для стобца InvoiceDate: {count_different_values(data, "InvoiceDate")}')
    print(f'Общее кол-во проданного товара для StockCode 21162: {get_total_quantity(data, 21161)}\n')

    data2 = MathStats(FILE2)
    print(f'Средние значения инвойсов: {data2.get_mean(data2.data)}')
    print(f'Максимальные значения инвойсов: {data2.max}')
    print(f'Минимальные значения инвойсов: {data2.min}')
    print(f'Дисперсии инвойсов: {data2.disp}')
    print(f'Среднеквадратические отклонения инвойсов: {data2.sigma_sq}\n')


def read_data(file: str) -> List[dict]:
    # считывание данных и возвращение значений в виде списка из словарей
    import csv
    data = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for _r in reader:
            row = {
                'InvoiceNo': int(_r['InvoiceNo']),
                'InvoiceDate': _r['InvoiceDate'],
                'StockCode': int(_r['StockCode']),
                'Quantity': int(_r['Quantity'])
            }
            data.append(row)
    return data


def count_invoice(data: List[dict]) -> int:
    count = 0
    # 1. Создаем список виденных инвойсов (пустой), пробегаемся по
    # data и если в списке нет очередного инвойса, то добавляем его туда
    # в конце считаем сколько элементов в нем есть.

    # 2. Создаем множество и добавляем туда по очереди все встреченные
    # элементы. Поскольку это множество, инвойсы в нем не будут
    # повторяться. В конце считаем сколько элементов.

    # > 3. Counter 
    # Реализуем получение номер invoices и помещение их в список
    # Переписать через генератор списка
    from collections import Counter
    invoices = [_el['InvoiceNo'] for _el in data]
    count = len(Counter(invoices))
    return count


def count_different_values(data: List[dict], key: str) -> int:
    """
    Функция должна возвращать число различных значений для столбца key в списке data

    key - InvoiceNo или InvoiceDate или StockCode
    """
    from collections import Counter
    key_count = [_el[key] for _el in data]
    count = len(Counter(key_count))
    return count


def get_total_quantity(data: List[dict], stock_code: int) -> int:
    """
    Возвращает общее количество проданного товара для данного stock_code
    """
    result = sum([_el['Quantity'] for _el in data if _el['StockCode'] == stock_code])
    return result


def Marketing_graph():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_csv('MarketingSpend.csv')
    j = data.iloc[0, 0][:-3]
    lst_sum_off = []
    lst_sum_on = []
    sum_off = 0
    sum_on = 0
    for i in range(365):
        if j == data.iloc[i, 0][:-3]:
            sum_off += data.iloc[i, 1]
            sum_on += data.iloc[i, 2]
        else:
            lst_sum_off.append(round(sum_off, 2))
            lst_sum_on.append(round(sum_on, 2))
            sum_off = 0
            sum_on = 0
            j = data.iloc[i, 0][:-3]
    lst_sum_off.append(sum_off)
    lst_sum_on.append(sum_on)

    months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
    spend_values = {
        'offline': np.array(lst_sum_off),
        'online': np.array(lst_sum_on),
    }
    sum = spend_values['offline'] + spend_values['online']

    fig, ax = plt.subplots(figsize=(12, 10))
    left = np.zeros(12)
    
    bars = ax.barh(months, sum, alpha=None)
    ax.bar_label(bars)

    for mode, value in spend_values.items():
        p = ax.barh(months, value, label=mode, left=left)
        left += value

        ax.bar_label(p, label_type='center')
    plt.legend(loc='best')
    
    plt.show()

def Retail_graph():
    import matplotlib.pyplot as plt
    import pandas as pd
    from datetime import datetime, timedelta

    data = pd.read_csv('Retail.csv')
    date_string = data.iloc[0, 1]
    j = datetime.strptime(date_string, "%Y-%m-%d").date()
    lst_sum_all = []
    sum_per_day = 0
    k = 0
    for i in range(data.shape[0]):
        if str(j) == data.iloc[i, 1]:
            sum_per_day += data.iloc[i, 3]
        else:
            lst_sum_all.append(sum_per_day)
            sum_per_day = 0
            j += timedelta(days=1)
            k += 1
    lst_sum_all.append(sum_per_day)

    fig, ax = plt.subplots(figsize=(12, 10))
    plt.scatter(list(range(1, 366)), lst_sum_all)
    plt.xlabel('Дни')
    plt.ylabel('Количество в день')
    plt.show()


if __name__ == "__main__":
    main()
    Marketing_graph()
    Retail_graph()
