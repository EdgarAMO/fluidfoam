from fluidfoam import readmesh
from fluidfoam import readvector
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import numpy as np

sol = '/home/edgar/OpenFOAM/edgar-7/run/actuatorCylinderA'

# coordinates
x, y, z = readmesh(sol, False)

# velocity field
vel = readvector(sol, '1200', 'U', False)

# flip them around
X = x.reshape(240, 920)
Y = y.reshape(240, 920)
Y = Y[::-1, :]

# magnitude of the velocity field
magU = np.sqrt( vel[0, :]**2 + vel[1, :]**2 )
magU.resize(240, 920)
magU = magU[::-1, :]

# circle represents the turbine
circle = Circle((0,0), 5.0, color='black', fill=False)

# plot the contours
fig = plt.figure(figsize=(6, 1.5))
plt.rc('font', size=18)
plt.rcParams["font.family"] = "monospace"
plt.title('VAWT wake @ TSR=6.0')
plt.xlabel('x')
plt.ylabel('y')
ax = fig.add_subplot(1,1,1)
img = ax.imshow(magU,
                interpolation='bilinear',
                cmap='jet',
                extent=[X.min(), X.max(), Y.min(), Y.max()])
cbar = fig.colorbar(ax=ax,
                    mappable=img,
                    orientation='horizontal',
                    pad=0.3,
                    label='m/s')
ax.add_artist(circle)
plt.show()


