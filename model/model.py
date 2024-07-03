import networkx as nx
from database.DAO import DAO
class Model:
    def __init__(self):
        self._aeroporti = DAO.getAllAeroporti()
        self._idMap = {}
        for a in self._aeroporti:
            self._idMap[a.ID]=a
        _

    def addEdge(self,miglia):
        self._grafo.clear()
        self._allEdges=DAO.getAllConnessioniTraAeroporti(self._idMap,miglia)
        self._grafo.add_edges_from(self._allEdges)
        return self._grafo.number_of_nodes(), self._grafo.number_of_edges(),self._grafo.edges

    def getAvgDist(self,v1,v2):
        data = self._grafo.get_edge_data(v1,v2)
        return data["weight"]





