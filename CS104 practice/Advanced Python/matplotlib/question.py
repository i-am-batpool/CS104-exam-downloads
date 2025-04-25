'''
    Distributions
'''

import numpy as np
from matplotlib import pyplot as plt

# Seeding for reproducibility
rng = np.random.default_rng(12345)
S=1500000
# sampling from each of the six distributions
beta=100*rng.beta(a=4, b=20, size=S)
expo=100*rng.exponential(scale=0.1, size=S)
gam=100*rng.gamma(shape=2, scale=0.1, size=S)
lap=100*rng.laplace(loc=0, scale=0.5, size=S)
normal=rng.normal(loc=0, scale=3, size=S)
pois=rng.poisson(lam=3, size=S)



# plotting histograms for each of the distributions
plt.subplot(3,2,1)
plt.hist(beta, bins=100, range=(-5,50), color="red")
plt.title("Beta")

plt.subplot(3,2,2)
plt.hist(expo, bins=100, range=(-1,50), color="green", alpha=0.5) #alpha is often called blending factor
plt.title("Exponential")

plt.subplot(3,2,3)
plt.hist(gam, bins=np.arange(-1,50,1), color="black", alpha=0.8, orientation="horizontal")
plt.title("Gamma")

plt.subplot(3,2,4)
plt.hist(lap, bins=np.arange(-1,50,1), color="orange")
plt.title("Laplace")

plt.subplot(3,2,5)
plt.hist(normal, bins=np.arange(-10,11,1))
plt.title("Normal")

plt.subplot(3,2,6)
plt.hist(pois, bins=np.arange(-1,11,1)) #this is how you should do when step and range are given
plt.title("Poisson")
# adjust the sub-plots to fit the titles and labels
plt.tight_layout()
# save the plot as plot.png
plt.savefig('plot.png')
