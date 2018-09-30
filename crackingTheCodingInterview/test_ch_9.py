from ch_9 import *
import unittest
import time

# I wanted to test copy_sorted_buffer() on random data, but I
# couldn't find the python random number generator since I was
# working on this during a flight, so I made my own based on
# a vague recollection of an alogrithm Von Neumann came up with
# in the 50's or 60's.
# The algorithm relies on the order of integers in a long base10
# number being somewhat independant of the numberline they exist on
# 91 and 19 are "close" in the "bytes-used-to-represent-the-number-in-a-string"
# space, but very far in the base10 number space. Thus, any sensible algorithm
# that fiddles with the order of digits in a number to generate new numbers
# will be somewhat random for a time. In a given run (based on a single seed),
# the pattern will repeat eventually, depending on the length of the base10
# representation of the initial seed, however, since I'm passing in the current
# time in nanoseconds each time it's called, we needn't worry about that. There
# are many other faults to this method too, but they aren't relevant here.
# Testing for how random the output is is out of the scope of testing copy_sorted_buffer()
# so I looked at it and found it to be sufficiently random for my purpose.
def random_numbers(n, seed=time.time_ns()):
    retArray = []
    for i in range(n):
        seed = [c for c in str(seed)]
        locOfMid = int(len(seed)/2)
        mid1 = int("".join(seed[locOfMid - 2:locOfMid]))
        mid2 = int("".join(seed[locOfMid:locOfMid + 2]))
        del seed[locOfMid - 2:locOfMid]
        seed.append(str(mid1*mid2))
        seed = int("".join(seed))
        retArray.append(seed)
    return retArray

class test_ch_9(unittest.TestCase):
    def test_copy_sorted_buffer(self):
        rand1 = random_numbers(3)
        rand2 = random_numbers(2)
        self.assertEqual(copy_sorted_buffer(sorted(rand1), sorted(rand2)), sorted(rand1 + rand2))
        rand1 = random_numbers(30)
        rand2 = random_numbers(100)
        self.assertEqual(copy_sorted_buffer(sorted(rand1), sorted(rand2)), sorted(rand1 + rand2))

if __name__ == '__main__':
    unittest.main()
