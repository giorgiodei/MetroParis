from model.fermata import Fermata
from model.model import Model

model = Model()
model.buildGrafoPesato()
print("Numero nodi:", model.getNumNodi())
print("Numero archi:", model.getNumArchi())

source= Fermata(2,"Abbesses", 2.33855,48.8843)
nodiBFS=model.getBFSNodesFromTree(source)
print(len(nodiBFS))
for i in range (0,10):
    print(nodiBFS[i])
nodiDFS=model.getDFSNodesFromEdges(source)
print(len(nodiDFS))
for i in range (0,10):
    print(nodiDFS[i])

print("---------------------------------------")

print("archi con peso 2:")
archiMaggiori=model.getArchiPesoMaggiore()
for a in archiMaggiori:
    print(a[0], "-->", a[1],":",a[2])
