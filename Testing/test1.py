import unittest

from test import anagram

class Test(unittest.TestCase):
    
    def test(self):

        read = open('Testing/test2.txt')
        s = read.readline(1)
        t = read.readline(2)
        read.close()
        self.assertTrue(anagram(s, t))