import unittest
import json
import os
import os.path
import sys
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
from GraphNode import GraphNode
from SocialGraph import SocialGraph


class SocialGraphTest(unittest.TestCase):
    mGraph = None
    mJsonDict = None

    def setUp(self):
        fname = os.path.join(testdir, "data", "testSGraph.json")
        self.mGraph = SocialGraph.createGraph(fname)
        self.mJsonDict = dict()
        with open(fname) as f:
            for line in f:
                entry = json.loads(line)
                self.mJsonDict[entry["user"]] = GraphNode(entry)

    def test_Ids(self):
        expected = set(list(self.mJsonDict.keys()))
        actual = set(self.mGraph.getIdList())
        # Should be the same length
        self.assertEqual(len(expected), len(actual), "Wrong number of ids in social graph.")
        # Shoule be the same
        self.assertTrue(len(expected - actual) == 0, "Mismatch between expected and actual.")

class GraphNodeTest(unittest.TestCase):
    mJson = None
    def setUp(self):
        self.mJson = list()
        self.mJson.append(json.loads('{"user": 1029394, "friends": [596680], "skill": 1}'))
        self.mJson.append(json.loads('{"user": 1029395, "friends": [69115,89673,176794,207524,214360,250646,377531,476673,485734,550592,701473,713199,734481,841171,921476], "skill": 4}'))
        self.mJson.append(json.loads('{"user": 1029396, "friends": [177524,286246,329758,365336,460601,550981,553141,615993,625422,678778,695472,734619,801722,833843,863810,899260,935183], "skill": 3}'))
        self.mJson.append(json.loads('{"user": 1029398, "friends": [163192,187767,300104,406631,716816], "skill": 0}'))
        self.mJson.append(json.loads('{"user": 1029401, "friends": [2616,5638,7818,20372,33205,65769,74650,81227,85700,87830,115089,154171,173169,179110,182353,222982,231149,243103,245277,246913,248909,253071,284568,293695,315954,334695,349210,367168,369724,403512,429930,439050,453861,470533,470868,480867,494303,499420,513098,519762,529614,533267,534868,579800,625902,669266,670856,675404,703027,742552,753311,767097,767893,785960,791744,804814,832718,880711,885735,897901,913225,927778,935101,944530,960221,968793,980611,1006736,1008143,1017346], "skill": 555}'))
        self.mJson.append(json.loads('{"user": 1029406, "friends": [14481,22235,118296,339721,394217,576303,581807,611581,645748,722240,876454,887127,1014269], "skill": 3}'))
        self.mJson.append(json.loads('{"user": 1029417, "friends": [305571,707747,798283], "skill": 0}'))
        self.mJson.append(json.loads('{"user": 1029418, "friends": [35466,49193,52197,134731,302303,412810,462677,504610,514312,533026,772124], "skill": 0}'))

    def test_user(self):
        keys = set()
        ids = set()
        for j in self.mJson:
            keys.add(j["user"])
            ids.add(GraphNode(j).getId())
        self.assertTrue(len(keys) == len(ids) and len(keys) > 0,
                        "Ether keys and ids don't match, or lenght is 0.")
        self.assertTrue(len(keys - ids) == 0, "A GraphNode is missing an id")
        self.assertTrue(len(ids - keys) == 0, "Got an extra id from a GraphNode.")



if __name__ == "__main__":
    unittest.main()

            
            
