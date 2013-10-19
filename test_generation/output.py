'''
    Nguyen Thi Loan
    MSSV: 10020197
    Lop: K55C-CLC
'''
import unittest
from input import main
import inspect
import string
import re
from random import randint
import itertools
 
# get doc string in main()
docstring = inspect.getdoc(main)

# number of variable in main()
numberOfVar = len(string.split(docstring))
    
# get numbers in doc string
ranges = re.findall(r'\d+', docstring)
    
# get the list that includes random values in each ranges
listValues = []
for i in range(len(ranges)):
    if (i%2==0):
        listValues.insert(i/2, randint(int(ranges[i]),int(ranges[i+1])))
            
    # get the list that includes numbers of equivalence class of each variable
docstr = string.split(docstring)
numberOfEquiv = []
for j in range(numberOfVar):
    numberOfEquiv.insert(j, docstr[j].count(';'))
    
# get the list that includes values to test
listTest = []
values = []
for k in range(len(numberOfEquiv)):
    values.insert(k, sum(numberOfEquiv[0:(k+1)]))
    
listTest.append(listValues[0:values[0]])
for h in range(len(numberOfEquiv)-1):
    listTest.insert(h, listValues[values[h]:values[h+1]])
    
listTest1 = list(itertools.product(*listTest))

# ********************************************

class TestSequence(unittest.TestCase):
    pass

def test_generation(a,b):
    def test(self):
        self.assertEqual(a,b)
    return test

l=0
if __name__ == '__main__':
        for t in listTest1:
            test_name = 'test'+str(l)
            test = test_generation(main(*t),"Not a triangle")
            setattr(TestSequence, test_name, test)
            l = l+1
        unittest.main()
         


