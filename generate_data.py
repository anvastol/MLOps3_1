import pandas as pd
import numpy as np
import os

if not os.path.exists('data'):
    os.makedirs('data')
# Создаем DataFrame с произвольными данными
data = {
    'feature1': np.random.rand(100),
    'feature2': np.random.rand(100),
    'label': np.random.randint(0, 2, 100)
}

df = pd.DataFrame(data)

# Сохраняем в файл
df.to_csv('data/dataset.csv', index=False)