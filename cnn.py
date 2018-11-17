import numpy as np
from keras.models import Model 
import keras
import pickle

# def unpickle(file):
#     with open(file, 'rb') as fo:
#         dict = pickle.load(fo,encoding='latin1')
#     return dict

# filepath = "./cifar-10/data_batch_2"
# dict = unpickle(filepath)
# for key,item in dict.items():
# 	print(key)

# batch_label = dict['batch_label']
# filenames = dict['filenames']
# data = dict['data']
# labels = dict['labels']

# print(type(data),data.shape,type(filenames),len(filenames),'\n',batch_label)

# unique = list()
# for i in labels:
# 	if i not in unique:
# 		unique.append(i)
# unique = sorted(unique)
# print (unique)
# num_occur = np.zeros(10)

# for i in labels:
# 	num_occur[i] += 1

(x_train, y_train), (x_test, y_test)=keras.datasets.cifar10.load_data()
# (x_train, y_train), (x_test, y_test) = (100,10),(343,5)
pickle_file =  './cifar10_keras.pickle'
try:
	f = open(pickle_file, 'wb')
	save = {
	'x_train': x_train,
	'x_test': x_test,
	'y_train': y_train,
	'y_test': y_test,
	}
	pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)
	f.close()
except Exception as e:
	print('Unable to save data to', pickle_file, ':', e)
	raise

f = open(pickle_file,'rb')
dic = pickle.load(f,encoding  = 'latin1')
print (dic)