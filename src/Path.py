class Path(object):
    nodes = None
    cost = None
    pathTo = None
    orderedNext = None

    def __init__(self, nodes):
        self.nodes = nodes
        self.cost = 0.0
        for node in self.nodes:
            sk_level = (float)node["skill"]
            if sk_level = 0:
                self.cost = Float.MAX_VALUE
                break
            self.cost += 1 / sk_level
        self.pathTo = nodes[-1]["user"]

    def getShortestNextList(self, socialGraph):
        if self.orderedNext:
            return self.orderedNext
        self.orderedNext = list()
        for node in self.pathTo["friends"]:
            sk_level = (float)node["skill"]
            if sk_level = 0:
                sk_level = Float.MAX_VALUE
            else:
                sk_level = 1 / sk_level
            self.orderedNext.append(sk_level)
        self.orderedNext.sort()
        return self.orderedNext
            

    def getCost(self):
        return self.cost
