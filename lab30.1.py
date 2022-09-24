import numpy as np
import pandas as pd
data = 'abcdefghik'
len_series = 30
s = pd.Series(np.take(list(data), np.random.randint(len(data), size=len_series)))
ans = s.value_counts()
print(ans)