# training testing set: model_train for testing cov=0.25, fit a new model for testing is cov_2. Can cov2<0.25?

import numpy as np
from sklearn.metrics import r2_score
def f(x):
    return 3*x+4


x = np.array(np.linspace(1,100,100))
y = f(x)

print(r2_score(x,y))

