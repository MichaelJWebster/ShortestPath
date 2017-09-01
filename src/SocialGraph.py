import logging
import json
from GraphNode import GraphNode

class SocialGraph(object):
    gDict = None

    @staticmethod
    def createGraph(fname):
        graphDict = dict()
        with open(fname) as f:
            for line in f:
                entry = json.loads(line)
                graphDict[entry["user"]] = GraphNode(entry)
        return SocialGraph(graphDict)
        
    def __init__(self, userDict):
        logging.basicConfig(level=logging.DEBUG)
        self.gDict = userDict
    
    def getUser(self, id):
        rval = None
        try:
            rval = self.gDict[id]
        except KeyError as ke:
            logging.error("getUser: Unknown Id requested: %d\n" % id)
            logging.error("%s" % ke)
            raise ke
        return rval

    def getIdList(self):
        idList = list()
        for k in self.gDict.keys():
            idList.append(k)
        return idList

    def resetGraph(self):
        for node in self.gDict.values():
            node.reset()

if __name__ == "__main__":
    fname = "../data/task.json"
    graph = SocialGraph.createGraph(fname)
    user = graph.getUser(1029419)
    print("User is %d => %s" % (1029419, user))
    l = graph.getIdList()
    print("100 Entries = %s\n" % l[:100])


        

        

            
            
        
