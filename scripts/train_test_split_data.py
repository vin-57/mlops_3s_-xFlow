import pandas as pd
import numpy as np
 
# Считываем из файла 
df = pd.read_csv('/home/sflow-admin/project/datasets/data_processed.csv', header=None)

# Разделяем на тренировочную и тестовую выборки
idxs = np.array(df.index.values)
np.random.shuffle(idxs)
l = int(len(df) * 0.7)
train_idxs = idxs[:l]
test_idxs = idxs[l+1:]
 
# Записываем в файл
df.loc[train_idxs, :].to_csv('/home/sflow-admin/project/datasets/data_train.csv')
df.loc[test_idxs, :].to_csv('/home/sflow-admin/project/datasets/data_test.csv')