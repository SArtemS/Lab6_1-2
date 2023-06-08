# (2843.5616438356165,  1905.8807397260264)
#  2843.5616438356165 # 1905.8807397260273
import pandas as pd
from mathstats import *

data = pd.read_csv('MarketingSpend.csv')
FILE2 = 'MarketingSpend.csv'
data2 = MathStats(FILE2)

def test_pandas_mean_vals():
    assert data2.get_mean(data2.data)['offline'] == round(data.loc[:, 'Offline Spend'].mean(), 2), " Неверное среднее значение offline инвойсов"
    assert data2.get_mean(data2.data)['online'] == round(data.loc[:, 'Online Spend'].mean(), 2), " Неверное среднее значение online инвойсов"

    
def test_pandas_max_vals():
    assert data2.max['offline'] == round(data.loc[:, 'Offline Spend'].max(), 2), " Неверное среднее значение offline инвойсов"
    assert data2.max['online'] == round(data.loc[:, 'Online Spend'].max(), 2), " Неверное среднее значение online инвойсов"  


def test_pandas_min_vals():
    assert data2.min['offline'] == round(data.loc[:, 'Offline Spend'].min(), 2), " Неверное среднее значение offline инвойсов"
    assert data2.min['online'] == round(data.loc[:, 'Online Spend'].min(), 2), " Неверное среднее значение online инвойсов"  
    

test_pandas_mean_vals()
test_pandas_max_vals()
test_pandas_min_vals()
