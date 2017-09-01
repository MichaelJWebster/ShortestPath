import logging
from SocialGraph import SocialGraph

class ShortestPath(object):
    mSocialGraph = None
    mVisited = None
    mSrcUser = None
    mTargetUser = None

    # Allow us to vary the weight we'll give to links with skill level 0.
    mZeroVal = 2.0

    def __init__(self, fname, zeroVal=2.0):
        logging.basicConfig(level=logging.DEBUG)
        self.mSocialGraph = SocialGraph.createGraph(fname)
        self.mZeroVal = float(zeroVal)

    def findShortestPath(self, start, finish):
        self.mSocialGraph.resetGraph()
        self.mVisited = list()
        self.mSrcUser = start
        self.mTargetUser = finish
        startNode = self.mSocialGraph.getUser(start)
        startNode.setVisited(None, 0, 0)
        startNode.setCost(0)
        for f in startNode.getFriends():
            node = self.mSocialGraph.getUser(f)
            skill = float(node.getSkill())
            cost = None
            if skill == 0:
                cost = self.mZeroVal
            else:
                cost = 1 / skill
            node.setVisited(startNode, 0, cost)
            self.mVisited.append(node)

        if self.getShortest():
            sPath = list()
            curUser = self.mTargetUser
            while curUser != self.mSrcUser:
                sPath.insert(0, curUser)
                curUser = self.mSocialGraph.getUser(curUser).getPrev().getId()
            sPath.insert(0, self.mSrcUser)
            return sPath
        else:
            logging.error("Couldn't find a path between %d and %d" % (start, finish))
            return None


    def getShortest(self):
        if len(self.mVisited) == 0:
            return self.mSocialGraph.getUser(self.mTargetUser).isVisited()
        else:
            visited = self.mVisited
            self.mVisited = list()
            for v in visited:
                for f in v.getFriends():
                    friend = self.mSocialGraph.getUser(f)
                    skill = float(friend.getSkill())
                    cost = None
                    if skill == 0:
                        cost = self.mZeroVal
                    else:
                        cost = 1 / skill
                    if friend.isVisited():
                        if friend.cost() > v.cost() + cost:
                            friend.setVisited(v, v.cost(), cost)
                        else:
                            continue
                    else:
                        friend.setVisited(v, v.cost(), cost)
                    self.mVisited.append(friend)
            return self.getShortest()



        
if __name__ == "__main__":
    fname = "../data/task.json"
    s = 1
    e = 7271
    sp = ShortestPath(fname)
    p = sp.findShortestPath(s, e)
    print("Shortest Path is: %s\n" % p)

