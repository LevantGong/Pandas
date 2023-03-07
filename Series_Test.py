import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5))
print(s)
print("index:")
#print(s.axes)
#print(s.dtype)
#print(s.empty)
#print(s.ndim)
#print(s.size)
#print(s.values)
print(s.index)
