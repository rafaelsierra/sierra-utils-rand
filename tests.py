# -*- coding: utf-8 -*-
import re
import time
import unittest
from sierra.utils.rand import get_random_string, stringsets

class TestRandomness(unittest.TestCase):
    
    def test_size_of_return(self):
        for x in xrange(1, 101):
            self.assertEqual(len(get_random_string(x)), x)

            
    def test_invalid_size(self):
        for x in xrange(0,-100, -1):
            self.assertIsNone(get_random_string(x))


    def test_performance(self):
        # Report for string of 10, 50 and 100 characters
        print 
        for length in [10, 50, 100]:
            start = time.time()
            for x in xrange(1, 501):
                get_random_string(length)
            total = time.time()-start
            print('Size {}: {} str/sec'.format(length, 500/total))
    
        
    def test_letters_only(self):
        pat = re.compile('^[a-z]+$', re.I)
        for x in xrange(1, 101):
            string = get_random_string(50, only_letters=True)
            self.assertTrue(pat.match(string))
    
        
    def test_letters_only(self):
        pat = re.compile('^[a-z0-9]+$', re.I)
        for x in xrange(1, 101):
            string = get_random_string(50, letters_and_numbers=True)
            self.assertTrue(pat.match(string))
    
    
    def test_homoglyph_safe(self):
        pat = re.compile('[i1lI0oO]')
        for x in xrange(1,101):
            string = get_random_string(50, stringset=stringsets.HOMOGLYPH_SAFE)
            self.assertFalse(pat.match(string))
            
            
    def test_ignoreset(self):
        for x in xrange(1,101):
            string = get_random_string(50, 'aeiou', ignoreset='i')
            self.assertNotIn('i', string)
        

    def test_stringset_as_iterable(self):
        self.assertTrue(get_random_string(5, stringset=['a','b','c']))
        self.assertTrue(get_random_string(5, stringset=('a','b','c')))
        self.assertTrue(get_random_string(5, stringset=set(['a','b','c'])))                
    

if __name__ == '__main__':
    unittest.main()