# -*- coding: utf-8 -*-
"""Assignment3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y30ep7ptvJkd-A0cZaHDC1ucLv8sXY7r
"""

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-5,5,100)

y_1 = x-1 #straight line1
y_2 = 0.25*x+0.5 #straighe line2
plt.plot(x, y_1, label='x-y-1=0')
plt.plot(x, y_2, label='x-4y+2=0')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid()
plt.show()