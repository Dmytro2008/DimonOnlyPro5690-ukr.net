import matplotlib.pyplot as PLT

fig, ax = PLT.subplots()
ax.imshow(checkerboard, cmap=PLT.cm.gray, interpolation='nearest')
PLT.show()