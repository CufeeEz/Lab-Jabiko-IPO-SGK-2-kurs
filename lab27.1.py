import pandas as pd
Series = pd.Series(['m','o','g','i','l','e','v'])
print(Series)
newSeries = Series.map(lambda x: x[0].upper() + x[1:-1])
print(newSeries)