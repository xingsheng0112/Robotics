#! /usr/bin/env python

import numpy as np
import pylab as plt
import csv

time_stamp = []
num_list = []
receve_list= []

for t in range(0,46,1):
    d = (2.0 * t) + ( t**2.0 )
    num_list.append(d)
    receve_list.append(d)
    time_stamp.append(t)

for i in range(0,46,1):
    receve_list[i] = round(num_list[i] + np.random.normal(0, 20),5)
print(num_list)
print(receve_list)

with open('/home/bbq/Desktop/output.csv', 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(num_list)
  writer.writerow(receve_list)


plt.figure(figsize=(6,8))
plt.subplot(211)
plt.title('The Original Signal')
plt.plot(time_stamp[0:46],num_list[0:46])

plt.subplot(212)
plt.title('Noise Signal')
plt.plot(time_stamp[0:46],receve_list[0:46])

plt.show()
plt.tight_layout()
