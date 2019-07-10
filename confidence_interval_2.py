import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import scipy.stats
import scipy.optimize
import scipy.spatial

poll=pd.read_csv("Statistics-Using-Python\data\poll.csv")
poll.info()
print (poll.vote.value_counts(normalize=True))

#sampling func
# ============
def sample(brown,n=1000):
    return pd.DataFrame({'vote':np.where(np.random.rand(n) <brown,'Brown','Green')})

s=sample(0.51,n=1000)
print(s.vote.value_counts(normalize=True))

dist=pd.DataFrame([sample(0.51).vote.value_counts(normalize=True) for i in range(1000)])
print (dist.head())

dist.Brown.hist(histtype='step',bins=20)
plt.show()