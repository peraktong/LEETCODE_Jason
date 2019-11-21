# A worm, next time it can die, remain the same, or split into 2 worms, each with equal probability.
# What’s the probability that it will die after infinite time?

# simulation:


import numpy as np

def f(x1,x2):
    return 0.25*x1+0.75*x2

x1 = np.random.normal(0,0.2,1000)+np.array(np.linspace(0,1000,1000))
x2 = np.random.normal(0,0.2,1000)+np.array(np.linspace(500,1500,1000))

y = f(x1,x2)


