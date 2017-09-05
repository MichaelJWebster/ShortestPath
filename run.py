import argparse
import sys
from src import ShortestPath
from ShortestPath import ShortestPath

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find a shortest path through a social graph.")
    parser.add_argument("--fname", "-f", type=str, required=True,
                       help="The name of a file containing json social net data.")

    args = parser.parse_args()
    sp = ShortestPath(args.fname)
    s = None
    e = None
    while True:
        try:
            inp = input("\nPlease enter source and dest nodes separated by a space: ")
            s, e = inp.split()
            s = int(s)
            e = int(e)
        except EOFError:
            print("Finished.")
            sys.exit(0)
        print("Path from %d to %d == %s\n" % (s, e, sp.findShortestPath(s, e)))


    
                       
