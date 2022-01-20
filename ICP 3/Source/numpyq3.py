import numpy as np
from collections import Counter
x=np.random.randint(0,20,size=15)
print(x)
y = list(x)

z = Counter(y)
print(z)
print('The most common occured integer and its frequency respectively are: ')
print(z.most_common(1))
