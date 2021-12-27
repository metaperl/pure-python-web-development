import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('datatest.txt')
data['date'] = data.date.astype('datetime64[ns]')
data = data.set_index('date')

