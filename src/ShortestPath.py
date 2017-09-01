from Path import Path
from SocialGraph import SocialGraph

class ShortestPath(object):
    socialGraph = None
    unvisited = None
    visited = None

    def __init__(self, fname):
        self.socialGraph = SocialGraph.createGraph(fname)

    def findShortestPath(self, start, finish):
        return
