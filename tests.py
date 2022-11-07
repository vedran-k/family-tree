import unittest
from family_tree import *

class Test(unittest.TestCase):
    def test_empty_file(self):
        empty_input = []
        ft = FamilyTree(empty_input)
        ft.make_family()
        self.assertEqual(dict(), ft.family)

    def test_normal_file(self):
        f = open('in1.txt', 'r')
        inLines = f.readlines()
        f.close()
        ft = FamilyTree(inLines)
        ft.make_family()
        e = {'Robert': ['Joe'], 'John': ['Adam', 'Frank'], 'Steven': ['Marc', 'Robert'], 'Adam': ['Steven'],'Lukas': ['Leo']}
        self.assertEqual(ft.family,e)

    def test_error_file(self):
        f = open('in2.txt', 'r')
        inLines = f.readlines()
        f.close()
        ft = FamilyTree(inLines)
        self.assertRaises(Exception, FamilyTree.make_family)


if __name__ == '__main__':
    unittest.main()
