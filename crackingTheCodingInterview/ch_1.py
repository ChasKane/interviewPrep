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
# the null terminator '\0').
# INPUT: any string "any" length (note: untested with non-ascii chars)
# also, note that python strings aren't null terminated -- don't worry
# about adding one, my code adds one, then removes it upon return
# OUTPUT: reverse of input string, with 0 still as last char
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
    # https://github.com/ChasKane/sideProject-CPython
    # Here, you'll find full commentary explaining each line in detail!
    from ctypes import sizeof, c_void_p, c_char, c_long, c_int
    bytes_header_size = sizeof(c_void_p) * 3 + sizeof(c_long)
    string_header_size = bytes_header_size + sizeof(c_int) * 4
    S = (c_char * (len(s) + 1)).from_address(id(s) + string_header_size)
    S[-1] = 0
    t = 0
    while ord(S[t]):
        t += 1
    t -= 1
    h = 0
    while h < t:
        a = ord(S[h]); b = ord(S[t])
        a ^= b; b ^= a; a ^= b
        S[h] = a; S[t] = b
        h += 1; t -= 1
    return s
