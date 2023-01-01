import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# df = pd.read_csv('ml/final.csv', index_col=0)
# df['input_form'] = '__label__' + df['category'] + ' ' + df['title']
# df_train, df_test = train_test_split(df, test_size=0.05, stratify=df['category'], shuffle=True, random_state=42)
# df_train.to_csv('input_train.csv', index=False, header=False, columns=['input_form'])
# df_test.to_csv('input_test.csv', index=False, header=False, columns=['input_form'])

# model = fasttext.train_supervised(input='input_train.csv')
# model.save_model('model/model.bin')