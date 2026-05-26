from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo=nx.DiGraph()
        self._idMapFermate={}
        for f in self._fermate:
            self._idMapFermate[f.id_fermata] = f

    def buildGrafoPesato(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._fermate)
        self.addEdgesPesati()


    def addEdgesPesati(self):
        #riutilizzare il principio di funzionamento del metodo addEdges3
        #ma contando quante volte provo ad agggiungere l'arcp
        self._grafo.clear_edges()
        alledges=DAO.getAllFermate()
        for conn in alledges:
            u = self._idMapFermate[conn.id_stazP]
            v = self._idMapFermate[conn.id_stazA]
            self._grafo.add_edge(u, v)

            if self._grafo.has_edge(u, v):
                self._grafo[u][v]['weight'] += 1
            self._grafo.add_edge(v, u)

        else:
            self._grafo.add_edge(u,v,weight=1)

    def addEdgesPesativ2(self): #semplifica python ma complica la query (in questo caso non tanto)
        # delea il calcolo del peso a query sql
        self._grafo.clear_edges()
        alledgesWPeso = DAO.getAllFermatePesati()
        for e in alledgesWPeso:
            u=self._idMapFermate[e[0]]
            v=self._idMapFermate[e[1]]
            peso=e[2]
            self._grafo.add_edge(u, v, weight=peso)


    def getArchiPesoMaggiore(self):
        edges=self._grafo.edges(data=True)

        edgesMaggiori=[]
        for e in edges:
            if self._grafo.get_edge_data(e[0],e[1])["weight"]>1:
                edgesMaggiori.append(e)
        return edgesMaggiori









    def getBFSNodesFromEdges(self,source):
        archi=nx.bfs_edges(self._grafo,source)
        nodiBFS=[]
        for u, v in archi:
            nodiBFS.append(v)
        return nodiBFS

    def getDFSNodesFromEdges(self,source):
        archi=nx.dfs_edges(self._grafo,source)
        nodiDFS=[]
        for u, v in archi:
            nodiDFS.append(v)
        return nodiDFS

    def getBFSNodesFromTree(self,source):
        tree=nx.bfs_tree(source)
        archi=list(tree.edges())
        nodi=list(tree.nodes())
        return nodi

    def getDFSNodesFromTree(self,source):
        tree=nx.dfs_tree(source)
        archi=list(tree.edges())
        nodi=list(tree.nodes())
        return nodi

    def buildGraph(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._fermate) #popolo i nodi con le fermate
        self.addEdges2()


    def addEdges(self):
        for u in self._fermate:
            for v in self._fermate:
                if DAO.hasconn(u,v):
                    self._grafo.add_edge(u, v)

    def addEdges2(self):
        for u in self._fermate:
            for conn in DAO.getVicini(u):
                v=self._idMapFermate[conn.id_stazA]
                self._grafo.add_edge(u, v)

    """def addEdges3(self):
        addedges=DAO.getAllEdges()
            for conn in addedges:
                u=self._idMapFermate[conn.id_stazP]
                v=self._idMapFermate[conn.id_stazA]
                self._grafo.add_edge(u, v)"""


    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)


    @property
    def fermate(self):
        return self._fermate