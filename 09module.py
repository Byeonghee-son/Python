import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010,2021)
gdp = np.array([100,120,150,160,180,200,220,240,260,280,300])
sales = np.array([50,70,30,45,60,80,70,90,110,100,120])
prices = np.array([10,12,15,16,18,20,22,24,26,28,30])

fig = plt.figure()
ax1 = plt.subplot2grid((3,3),(2,0),1,3)
ax1.plot(years,gdp,marker='o',color='b')
ax1.set_title('GDP')
ax1.set_xlabel('Years')
ax1.set_ylabel('GDP(in billions)')

ax2 = plt.subplot2grid((3,3),(0,0),2,1)
ax2.scatter(years,prices,color='r')
ax2.set_xlabel('Years')
ax2.set_ylabel('Price')
ax2.set_title('Prices')

ax3 = plt.subplot2grid((3,3),(0,1),1,2)
ax3.bar(years,sales,color='g')
ax3.set_xlabel('Years')
ax3.set_ylabel('Quantity Sold')
ax3.set_title('Sales')

ax4 = plt.subplot2grid((3,3),(1,1),1,2)
ax4.plot(years,sales,color='b',marker='o')
ax4.set_xlabel('Years')
ax4.set_ylabel('Quantity Sold')
ax4.set_title('Sales')

plt.show()

# 단일 배열 저장
arr1 = np.array([1, 2, 3, 4, 5])
np.save('arr1.npy', arr1)

# 다중 배열 저장
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.array([10, 20, 30, 40, 50])
np.savez('arr.npz', arr2=arr2, arr3=arr3)

# 배열 불러오기
loaded_arr1 = np.load('arr1.npy')
loaded_data = np.load('arr.npz')
loaded_arr2 = loaded_data['arr2']
loaded_arr3 = loaded_data['arr3']


