# 9.1
# Given two sorted arrays A and B, and that A has space enough at the end
# of its buffer for B, merge B into A in sorted order.
# INPUT: list of integers
# OUTPUT: list of each of A's and B's integers in sorted order
def copy_sorted_buffer(A, B):
    # 1. How would I actually do this?
    # return sorted(A+B)
    # 2. If that's not allowed? use list.insert (non-array-like feature of python lists)
    # 3. if we weren't working in python, this is the kinda code I'd use:
    # startOfB = len(A)
    # A = A+B
    # for i in range(startOfB, len(A)):
    #     print(A)
    #     for j in range(i-1, -1, -1):
    #         if A[j] > A[j+1]:
    #             x = A[j]
    #             A[j] = A[j+1]
    #             A[j+1] = x
    #         else:
    #             break
    # return A

    # <reads solution> well, I did think of that, but I suppose I forgot about the idea
    # by the time I started coding...
    # 4. Better answer than (2) or (3) would be to start from the end of A (after extending
    # its buffer by the length of B) and simply merge the two in line, O(N+M) where N is
    # len(A) and M is len(B)
    i = len(A) - 1 # index of item currently being considered in A
    j = len(B) - 1 # index of item currently being considered in B
    k = len(A) + len(B) - 1 # index where we'll put the next selected item
    A = A + [0 for _ in range(len(B))]
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1
    while j >= 0:
        A[k] = B[j]
        k -= 1
        j -= 1
    return A

def 
