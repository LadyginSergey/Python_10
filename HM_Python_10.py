import pandas as pd
import random
#Импортируем библотеки 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Переводим данные в one hot вид
data_one_hot = data.apply(lambda x: x.astype('category').cat.codes)
data_one_hot = pd.concat([data_one_hot, 1 - data_one_hot], axis=1)
data_one_hot.columns = ['human', 'robot']

data_one_hot.head()
#