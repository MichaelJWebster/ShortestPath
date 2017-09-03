import logging
import math
from SocialGraph import SocialGraph

class ShortestPath(object):
    mSocialGraph = None
    mCandidate = None
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
        self.mCandidate = list()
        self.mSrcUser = start
        self.mTargetUser = finish
        startNode = self.mSocialGraph.getUser(start)
        startNode.setVisited()
        startNode.setCost(0, None)
        for f in startNode.getFriends():
            node = self.mSocialGraph.getUser(f)
            skill = float(node.getSkill())
            cost = None
            if skill == 0:
                cost = self.mZeroVal
            else:
                cost = 1 / skill
            node.setCost(cost, startNode)
            self.insertCandidateInOrder(node)

        if self.getShortest():
        #if self.getShortest2():
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
        while not self.mSocialGraph.getUser(self.mTargetUser).isVisited():
            if len(self.mCandidate) == 0:
                return False
            curNode = self.mCandidate.pop(0)
            if curNode.isVisited():
                continue
            curNode.setVisited()
            for f in curNode.getFriends():
                fnode = self.mSocialGraph.getUser(f)
                if not fnode.isVisited():
                    skill = float(fnode.getSkill())
                    cost = None
                    if skill == 0:
                        cost = self.mZeroVal
                    else:
                        cost = 1 / skill
                    if cost + curNode.cost() < fnode.cost():
                        fnode.setCost(cost + curNode.cost(), curNode)
                    self.insertCandidateInOrder(fnode)
        return True
                
    def insertCandidateInOrder(self, node):
        nodeCost = node.cost()
        if len(self.mCandidate) == 0:
            self.mCandidate.append(node)
        else:
            checkStart = 0
            checkEnd = len(self.mCandidate) - 1
            while True:
                if checkStart >= checkEnd:
                    if nodeCost > self.mCandidate[checkStart].cost():
                        self.mCandidate.insert(checkStart + 1, node)
                    else:
                        self.mCandidate.insert(checkStart, node)
                    return
                else:
                    mid = math.floor(checkStart + (checkEnd - checkStart)/2)
                    if self.mCandidate[mid].cost() > nodeCost:
                        checkEnd = mid - 1
                    else:
                        checkStart = mid + 1

            
    def getShortest2(self):
        if self.mSocialGraph.getUser(self.mTargetUser).isVisited():
            return True
        else:
            if len(self.mCandidate) == 0:
                return False
            candidates = self.mCandidate
            self.mCandidate = list()
            for c in candidates:
                for f in c.getFriends():
                    friend = self.mSocialGraph.getUser(f)
                    skill = float(friend.getSkill())
                    cost = None
                    if skill == 0:
                        cost = self.mZeroVal
                    else:
                        cost = 1 / skill
                    if friend.isVisited():
                        if friend.cost() > c.cost() + cost:
                            friend.setCost(c.cost() + cost, c)
                            friend.setVisited()
                        else:
                            continue
                    else:
                        friend.setCost(cost + c.cost(), c)
                        friend.setVisited()
                    self.mCandidate.append(friend)
            return self.getShortest2()

        
if __name__ == "__main__":
    fname = "../data/task.json"
    #fname = "../data/test1.json"
    #s = 4
    #e = 2
    s = 1
    e = 7271
    sp = ShortestPath(fname)
    p = sp.findShortestPath(s, e)
    print("Shortest Path is: %s\n" % p)

