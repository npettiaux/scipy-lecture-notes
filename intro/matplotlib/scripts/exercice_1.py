from pylab import *

n = 256
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
plot(X,C),plot(X,S)

#savefig("../figures/exercice_1.png",dpi=72)
show()
