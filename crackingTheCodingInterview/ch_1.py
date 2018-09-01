# 1.1
# Implement an algorithm to determine if a string has
# all unique characters. What if you can not use
# additional data structures?
# INPUT: string, "any" length, all lowercase letters
# OUTPUT: True, False
def unique_characters(s):
    # O(n) w/ data structure
    # x = {}
    # for c in s:
    #   if c in x: return False
    #   else: x[c] = 1
    # return True

    # O(n^2) w/o data structures (I didn't think of sorting
    # initially, but I think something like merge sort
    # would sorta meet the w/o data structures requirement.
    # Inner loop is hastened slightly from starting at x+1.
    for x in range(len(s)):
        for y in range(x+1, len(s)):
            if s[x] == s[y]: return False
    return True

# 1.2
# Write code to reverse a C-Style String (C-String means
# that “abcd” is represented as five characters, including
# the null character).
# INPUT: pre-formatted (last char is ' ' representing '\0')
# string, "any" length
# OUTPUT: reverse of input string, with ' ' still as last char
def c_reverse(s):
    # the point of this question is somewhat lost in Python,
    # but this was an excellent opportunity to learn about
    # cython from https://jasonstitt.com/mutable-python-strings
    # also super helpful:
    # https://github.com/python/cpython/blob/master/Include/object.h
    # and search `from_address` on this page once you get going:
    # https://github.com/python/cpython/blob/master/Doc/library/ctypes.rst
    # ... 3 hours later (said in bored pirate voice) ...
    # After fidling with this for a while, it seems silly to put here,
    # as it has caused seg faults (in Python!!! :D ), and isn't relevent
    # to the problem per say. I've moved this to a seperate repo:
    #

    return s
