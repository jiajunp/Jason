#/usr/bin/ptyhon
from pandas import *
import  numpy as np
import  matplotlib.pyplot as plt

from bs4 import  BeautifulSoup




s = Series(np.random.rand(10).cumsum(),index=np.arange(0,100,10))
#s.plot()
#plt.show(s.plot())
df = DataFrame(np.random.randn(10,4).cumsum(0),columns=['A','B','C','D'],index=np.arange(0,100,10))
#plt.show(df.plot())
df.plot()
plt.show()