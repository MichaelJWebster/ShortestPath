import logging
import sys

class GraphNode(object):
    mVisited = False
    mCost = sys.float_info.max
    mContents = None
    mPrev = None

    def __init__(self, jsonDict):
        self.mContents = jsonDict

    def reset(self):
        self.mVisited = False
        self.mCost = sys.float_info.max

    def setVisited(self):
        self.mVisited = True
        
    def isVisited(self):
        return self.mVisited

    def setTentative(self, fromNode, newCost):
        self.mPrev = fromNode
        self.mCost = newCost

    def getPrev(self):
        return self.mPrev

    def setCost(self, cost):
        self.mCost = cost
        
    def cost(self):
        return self.mCost

    def getFriends(self):
        return self.mContents["friends"]

    def getSkill(self):
        return self.mContents["skill"]

    def getId(self):
        return self.mContents["user"]

    def __str__(self):
        s = "User: %d\n" % self.mContents["user"]
        s = "%sCost = %.2E\n" % (s, self.mCost)
        s = "%sVisited = %s\n" % (s, self.mVisited)
        s = "%sFriends = %s\n" % (s, self.mContents["friends"])
        s = "%sSkill = %s\n" % (s, self.mContents["skill"])
        return s

        
    
