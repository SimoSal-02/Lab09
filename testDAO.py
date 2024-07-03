from database.DAO import DAO
from model.model import Model

aeroporti=DAO.getAllAeroporti()

modello = Model()

print(modello.addEdge("3000"))

print(DAO.getAllConnessioniTraAeroporti(modello._idMap,4000))
