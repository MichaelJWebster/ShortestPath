import logging
import json

class SocialGraph(object):
    gDict = None

    @staticmethod
    def createGraph(fname):
        graphDict = dict()
        with open(fname) as f:
            for line in f:
                entry = json.loads(line)
                graphDict[entry["user"]] = entry
        return SocialGraph(graphDict)
        
    def __init__(self, userDict):
        logging.basicConfig()        
        self.gDict = userDict
    
    def getUser(self, id):
        rval = None
        try:
            rval = self.gDict[id]
        except KeyError as ke:
            self.logger.error("getUser: Unknown Id requested: %d\n" % id)
            self.logger.error("%s" % ke)
            raise ke
        return rval

    def getIdList(self):
        idList = list()
        for k in self.gDict.keys():
            idList.append(k)
        return idList


if __name__ == "__main__":
    fname = "../data/task.json"
    graph = SocialGraph.createGraph(fname)
    user = graph.getUser(1029419)
    print("User is %d => %s" % (1029419, user))
    l = graph.getIdList()
    print("100 Entries = %s\n" % l[:100])
    

        

        

            
            
        
