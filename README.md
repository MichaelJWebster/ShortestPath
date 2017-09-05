# ShortestPath: Social Network Shortest Path task.

This repository contains code, documentation and some tests for the Data61
shortest path task.

The directory contents are:

.
./data
./data/task.json.gz
./data/test1.json
./data/test2.json
./doc
./doc/ShortestPathSocial.org
./doc/ShortestPathSocial.pdf
./README.md
./run.py
./src
./src/__init__.py
./src/GraphNode.py
./src/ShortestPath.py
./src/SocialGraph.py
./test
./test/__init__.py
./test/data
./test/data/test1.json
./test/data/testExample.json
./test/data/testSGraph.json
./test/spTest.py

## src

The src directory contains the python3 source.

## doc

The doc directory contains a small pdf describing the algorithm.

## data

The data directory contains some test files, and the gzipped task.json file.

## test

The test directory contains the python unittests.

## Run Tests

The tests are in the test/spTest.py file, and can be run as follows:

bash-3.2$ python3 test/spTest.py 
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK

## Running the code

The file ./run.py contains a main function to find a shortest path given
a file containing social network data. It loads the social network file, and
then repeatedly asks for start and end nodes. Ctrl-D ends it.

It can be run as follows:

bash-3.2$ python3 run.py -f data/test2.json 

Please enter source and dest nodes separated by a space: 1 6
Path from 1 to 6 == [1, 2, 4, 6]


Please enter source and dest nodes separated by a space: 3 6
Path from 3 to 6 == [3, 5, 6]


Please enter source and dest nodes separated by a space: Finished.



