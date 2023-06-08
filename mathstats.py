"""
Для вычисления дисперсии и ср. квадр. отклонения использовать 
https://myslide.ru/documents_3/b9d7b50c38e81a4b8b7645742d3b22c7/img10.jpg
"""


class MathStats():

    def __init__(self, file):
        import csv

        self._file = file
        self._data = []
        self._mean = None
        self._max = float('-Inf')
        self._min = float('Inf')
        with open(self._file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for _r in reader:
                row = {
                    'Date': _r[''],
                    'Offline': float(_r['Offline Spend']),
                    'Online': float(_r['Online Spend']),
                }
                self._data.append(row)

    @property
    def data(self):
        return self._data

    def get_mean(self, data):
        """
        Вычисление среднего по оффлайн и онлайн тратам
        """

        sums = {'offline': 0, 'online': 0}
        for _l in data:
            sums['offline'] += _l['Offline']
            sums['online'] += _l['Online']

        sums['offline'] = round(sums['offline'] / len(data), 2)
        sums['online'] = round(sums['online'] / len(data), 2)

        self._mean = sums

        return self._mean

    @property
    def max(self):
        # TODO
        maxs = {'offline': float('-Inf'), 'online': float('-Inf')}
        for _l in self._data:
            if _l['Offline'] > maxs['offline']:
                maxs['offline'] = round(_l['Offline'], 2)
            if _l['Online'] > maxs['online']:
                maxs['online'] = round(_l['Online'], 2)

        self._max = maxs

        return self._max

    @property
    def min(self):
        mins = {'offline': float('Inf'), 'online': float('Inf')}
        for _l in self._data:
            if _l['Offline'] < mins['offline']:
                mins['offline'] = round(_l['Offline'], 2)
            if _l['Online'] < mins['online']:
                mins['online'] = round(_l['Online'], 2)

        self._min = mins

        return self._min

    @property
    def disp(self):
        mean = self.get_mean(self._data)
        sums = {'offline': 0, 'online': 0}
        for _l in self._data:
            sums['offline'] += (_l['Offline'] - mean['offline']) * (_l['Offline'] - mean['offline'])
            sums['online'] += (_l['Online'] - mean['online']) * (_l['Online'] - mean['online'])
        sums['offline'] = round(sums['offline'] / len(self._data), 2)
        sums['online'] = round(sums['online'] / len(self._data), 2)

        self._disp = sums

        return self._disp

    # по аналогии — со среднем квадратичным отклонением
    @property
    def sigma_sq(self):
        from math import sqrt
        sums = {'offline': round(sqrt(self.disp['offline']), 2), 'online': round(sqrt(self.disp['online']), 2)}
        
        self._sigma_sq = sums
        
        return self._sigma_sq