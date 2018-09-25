# inspired by https://www.geeksforgeeks.org/python-tricks-competitive-coding/
# import statements are grouped with their relevant code section, contrary to
# convention

# Counter.most_common(n) returns the n most common items in a list
# in decreasing order of occurance, formated as a list of tuples in
# the format (item, frequency)
from collections import Counter
a = [1,2,3,4,5,6,1,2,3,4,2,3,1,3,2,4,5,3,4,2,3,4,5,2,4,5,5,4,5,1]
counter = Counter(a)
print(counter.most_common(3))

# nlargest/nsmallest from heapq each return the n largest/smallest elements
# in the iterable you give them, in decreasing/increasing order respectively.
# as with sorted, you can give it a key (function to call on each item once in
# the iterable, which can be used to grab a value from a key if you're trying to
# sort a list of dicts by a specific value
import heapq
a = [5,1,3,7,9,0,-4,-5,-6,-2,4,2,0,8]
print(heapq.nlargest(4, a))
print(heapq.nsmallest(6, a))

# zipping is fun
def zipper(*arg_list):
    print(arg_list)
list1 = [1, 2, 3]
list2 = [10, 20, 30]
z = zip(list1, list2)
tupple_list = [x for x in z]
zipper(tupple_list)

#unpacking things is cool
def unpack(*arg_list):
    print(arg_list)

# lists can be unpacked
l = [1, 2, 3, 4]
unpack(*l)
# so can iterables
unpack(*l.__iter__())
# so can dicts
unpack(*{"a": 42, "b": 43, "c": 44})
