import logging
import math
from SocialGraph import SocialGraph

class ShortestPath(object):
    """
    Implements a version of the shortest path algorithm.
    """
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
        """
        Create a path from a sequence of prev links from finish to start.

        Args:
        start    The start node of the path to be found
        finish   The end node of the path to be found.
        """
        sPath = list()
        curUser = finish
        while curUser != start:
            sPath.insert(0, curUser)
            curUser = self.mSocialGraph.getUser(curUser).getPrev().getId()
        sPath.insert(0, start)
        return sPath

    def findShortestPath(self, start, finish):
        """
        Return the shortest path between start and finish, by searching the
        mSocialGraph using a Dkikstra style algorithm.

        Args:
        start    The start node of the path to be found
        finish   The end node of the path to be found.

        Returns:
        A list containing the shortest path, or None if no path exists.
        """
        if start == self.mSrcUser and self.mSocialGraph.getUser(finish).isVisited():
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
        """
        The main part of the shortest path algorithm.
        """
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
        """
        Insert gNode in self.mNextShortest in (ascending) order by cost.

        Args:
        gNode   A GraphNode to be inserted.
        """
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
        """
        Return the skill weight for node as the inverse of it's skill level,
        or self.mZero if node's skill is 0.

        Args:
        node    The node we want a skill weight from.

        Returns:
        The integer value we're going to use as a weight on edges to node.
        """
        skillVal = float(node.getSkill())
        skillWeight = None
        if skillVal == 0:
            skillWeight = self.mZeroVal
        else:
            skillWeight = 1 / skillVal
        return skillWeight



