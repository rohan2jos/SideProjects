# test suite
# import statements
import unittest

import HTMLTestRunner
from Fibonacci import mainFunc
from clientsandservers.BubbleSort import  bubble
from mergeDemo import mainFunct

r = ''
class myTest(unittest.TestCase):
    def test(self):
        print "running test for bubble sort"
        res = self.assertEqual(bubble(), [1, 3, 5, 6, 7, 8, 9])
        return res

    def testMergeSort(self):
        print "running test for merge sort"
        self.assertEqual(mainFunct(), [0, 1, 3, 5, 9, 11, 33, 76, 77])

    def testFibonacci(self):
        print "running test for fibonacci"
        self.assertEqual(mainFunc(), [0, 1, 1, 2, 3])

def generateReport():
    suite = unittest.TestLoader().loadTestsFromTestCase(myTest)
    unittest.TextTestRunner(verbosity=2)
    output = open("results.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=output, title='Test report', description='report for the sorting')
    runner.run(suite)