import logging
import math
from SocialGraph import SocialGraph

class ShortestPath(object):
    mSocialGraph = None
    mNextShortest = None
    mSrcUser = None
    mTargetUser = None

    # Allow us to vary the weight we'll give to links with skill level 0.
    mZeroVal = 2.0

    # Record start node so we can quickly return results if start and finish
    # requested are on the previously searched path.
    mStart = None

    def __init__(self, fname, zeroVal=2.0):
        logging.basicConfig(level=logging.DEBUG)
        self.mSocialGraph = SocialGraph.createGraph(fname)
        self.mZeroVal = float(zeroVal)

    def unwindShortest(self, start, finish):
        sPath = list()
        curUser = finish
        while curUser != start:
            sPath.insert(0, curUser)
            curUser = self.mSocialGraph.getUser(curUser).getPrev().getId()
        sPath.insert(0, start)
        return sPath

    def findShortestPath(self, start, finish):
        if start == self.mSrcUser and self.mSocialGraph.getUser(finish).isVisited():
            print("Just returning already found path.")
            return self.unwindShortest(start, finish)
            
        self.mSocialGraph.resetGraph()
        self.mSrcUser = start
        self.mTargetUser = finish
        startNode = self.mSocialGraph.getUser(start)
        startNode.setTentative(None, 0)
        self.mNextShortest = [startNode]

        if self.getShortest():
            return self.unwindShortest(self.mSrcUser, self.mTargetUser)
        else:
            logging.error("Couldn't find a path between %d and %d" % (start, finish))
            return None


    def getShortest(self):
        while not self.mSocialGraph.getUser(self.mTargetUser).isVisited():
            if len(self.mNextShortest) == 0:
                return False
            nextNode = self.mNextShortest.pop(0)
            if nextNode.isVisited():
                continue
            nextNode.setVisited()
            
            for f in nextNode.getFriends():
                friend = self.mSocialGraph.getUser(f)
                skillWeight = self.getSkill(friend)
                newCost = skillWeight + nextNode.cost()
                if friend.cost() > newCost:
                    friend.setTentative(nextNode, newCost)
                else:
                    # No need to insert, it's already there.
                    continue
                self.insertNextInOrder(friend)
        return True

    def insertNextInOrder(self, gNode):
        if len(self.mNextShortest) == 0:
            self.mNextShortest.append(gNode)
            return
        start = 0
        end = len(self.mNextShortest) - 1
        while start <= end:
            mid = math.floor(start + (end - start)/2.0)
            if gNode.cost() > self.mNextShortest[mid].cost():
                start = mid + 1
            else:
                end = mid - 1
        self.mNextShortest.insert(start, gNode)

    def getSkill(self, node):
        skillVal = float(node.getSkill())
        skillWeight = None
        if skillVal == 0:
            skillWeight = self.mZeroVal
        else:
            skillWeight = 1 / skillVal
        return skillWeight

if __name__ == "__main__":
    fname = "../data/task.json"
    s = 1
    e = 7271
    # fname = "../data/test1.json"
    # s = 3
    # e = 2
    # fname = "../data/test2.json"
    # s = 1
    # e = 6    
    sp = ShortestPath(fname)
    p = sp.findShortestPath(s, e)
    print("Shortest Path is: %s\n" % p)    
    # e = 8
    # p = sp.findShortestPath(s, e)
    # print("Shortest Path is: %s\n" % p)
    # e = 4
    # p = sp.findShortestPath(s, e)
    # print("Shortest Path is: %s\n" % p)    




