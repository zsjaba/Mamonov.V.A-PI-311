# -*- coding: utf-8 -*-
"""Untitled61.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10_VrlYcfwI5O_yQ5xp702w2Gs3LYXqqw
"""

fahrenheit = [[-88.6], [-29.2], [32.0], [93.2], [129.2], [152.6], [212.0]]
kelvin = [[206.15], [239.15], [273.15], [307.15], [327.15], [340.15], [373.15]]

import matplotlib.pyplot as plt
plt.figure(figsize=(15,8), dpi=50)
plt.scatter(fahrenheit, kelvin, label='входные данные', color='green', marker='$f$');
plt.xlabel('fahrenheit')
plt.ylabel('kelvin')
plt.legend()
plt.grid(True)
plt.show()

for f,k in zip(fahrenheit, kelvin):
  print(f'фаренгейт {f} = кельвин{k}')

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(fahrenheit, kelvin) # входные данные
lr.predict([[256], [123]]) # проверка
lr.coef_
lr.intercept_
fahrenheit_test = [[-90], [-30], [32], [95], [130], [150], [210]]
kelvin_test = lr.predict(fahrenheit_test)
kelvin_test

#1
import numpy as np
x_range = np.arange(-90, 220)
y_range = (x_range+459.67) / 1.8
plt.figure(figsize=(15,8), dpi=280)
plt.plot(x_range, y_range, label='уравнение', linewidth='1')
plt.scatter(x_range, y_range, label='входные данные', color='green')
plt.scatter(fahrenheit_test, kelvin_test, label='предсказанное значение', color='blue')
plt.xlabel('Фаренгейта')
plt.ylabel('Кельвин')
plt.legend()
plt.grid(True)
plt.show()

#3/1
plt.bar([5], [3], label='кол.во кур')
plt.bar([3], [30], label='кол.во гусей')
plt.bar([4], [15], label='кол.во жирафов')
plt.legend()
plt.show()

#2
#https://github.com/zsjaba/Mamonov.V.A-PI-311/blob/main/Untitled6_1.ipynb

#3/2
data = [23, 17, 35]
cars = ['AUDI', 'BMW', 'FORD']
plt.pie (data, labels = cars)
plt.legend()
plt.show()

#3/3
plt.boxplot([[1, 5, 7, 4, 6, 10, 15],
             [-2, 5, 7, 4, 6, 10, 15],
             [-4, 5, 7, 4, 6, 10]])
plt.show()

#4/1
import math
math.e

#4/2
import math
math.pi

#4/3
import math
math.nan

#4/4
import math
math.factorial(13)

#4/5
import math
math.gcd(13, 32000000)

#1усл
import matplotlib.pyplot as plt
x= (0, 0.25, 0.25, 0.5,0.4, 1, 1.5, 2, 4.5, 5.5, 7.5,  8.5, 8.5,7.5,6, 7.25, 7.5,  7.4, 7.2, 7.3, 7.5,  6,    5.75,5.25,5,   4.5, 5.5,5.25,4.5, 3, 3.5, 3.2, 3, 2.5, 2,1.75, 1.5, 1, 0.75, 0 )
y= (3, 3.25, 3.5,  4,  4.5, 4, 3.5, 4, 4.25,3.25,4.25, 3,   2,  4,  3, 2.25, 1,    0.2, 0.2, 0.5, 1.25, 2.1, 1,   0.2, 0.2, 0.5, 1,  1.5, 2.5, 2.5, 0.5, 0.5, 2, 2.25, 0.2, 0.2, 2, 2.95, 2.75, 3)
plt.plot(x,y)
plt.show()

#2усл
import tensorflow as tf

image_data = tf.keras.datasets.fashion_mnist

from sys import platform
(train_images,train_labels),(test_images,test_labels) = image_data.load_data()

import matplotlib.pyplot as plt

plt.imshow(train_images[2])
#Данные должны быть предварительно обработаны перед обучением сети для этого масштабируйум эти значения в диапазоне от 0 до 1.

(train_images,train_labels),(test_images,test_labels) = image_data.load_data()
train_images = train_images / 255.0
test_images = test_images / 255.0
train_images[0]
#Загрузка набора данных возвращает четыре массива "train_images train_images test_images test_images"

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape =(28,28)),
    tf.keras.layers.Dense(128,activation="relu"),
    tf.keras.layers.Dense(10)
])
#tf.keras.Sequential Последовательная группировка линейного стека модулей
#tf.keras.layers является модулем; Dense and Flatten имеют параметры которые я нашел в интренете (._. ')

model.compile(optimizer="adam",
               loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
               metrics=["accuracy"]
)
#tf.keras.losses измеряет, насколько точна модель во время обучения
#optimizer="adam" менно так модель обновляется на основе данных, которые она видит, и ее функции потерь.
#metrics используется для мониторинга этапов обучения и тестирования
model.fit(train_images,train_labels,epochs=10)

model.predict(test_images)[0]
test_labels[0]
# train_images и train_labels представляют собой обучающий набор — данные, которые модель использует для обучения.