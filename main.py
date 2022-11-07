import sys
from family_tree import *

def main():
    for i in range(1, len(sys.argv)):
        f = open(sys.argv[i], 'r')
        inLines = f.readlines()
        f.close()
        ft = FamilyTree(inLines)
        ft.make_family()
        ft.find_parents()
        # uncomment for saving output to file
        #file_path = 'output.txt'
        #sys.stdout = open(file_path, "w")
        print_family_tree(ft.family, ft.parents)
        #sys.stdout.close()

if __name__ == '__main__':
    main()