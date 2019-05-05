
# coding: utf-8

# In[3]:


import func
import unittest
import os

Path = input()
filelist = os.listdir(Path)


# In[4]:


class TestRange(unittest.TestCase):
    def test_mood(self): 
        for i in filelist:
            path=Path+'/'+i
            if i.endswith(".txt"):
                self.assertTrue(func.mood_test(path) <=1 and func.mood_test(path)>=0)
    def test_kid(self):
        for i in filelist:
            path=Path+'/'+i
            if i.endswith(".txt"):
                self.assertTrue(func.kid_safe(path) <=1 and func.kid_safe(path)>=0)
    def test_length(self):
        for i in filelist:
            path=Path+'/'+i
            if i.endswith(".txt"):
                self.assertTrue(func.length_test(path) <=1 and func.length_test(path)>=0)
    def test_complexity(self):
        for i in filelist:
            path=Path+'/'+i
            if i.endswith(".txt"):
                self.assertTrue(func.complexity(path) <=1 and func.complexity(path)>=0)
    def test_love(self):
        for i in filelist:
            path=Path+'/'+i
            if i.endswith(".txt"):
                self.assertTrue(func.love_test(path) <=1 and func.love_test(path)>=0)               

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestRange)
# Run each test in suite
unittest.TextTestRunner().run(suite)

