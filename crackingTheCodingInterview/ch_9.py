# 9.1
# Given two sorted arrays A and B, and that A has space enough at the end
# of its buffer for B, merge B into A in sorted order.
# INPUT: list of integers
# OUTPUT: list of each of A's and B's integers in sorted order
def copy_sorted_buffer(A, B):
    # How would I actually do this?
    # return sorted(A+B)
    # If that's not allowed? use list.insert (non-array-like feature of python lists)
    startOfB = len(A)
    A = A+B
    for i in range(startOfB, len(A)):
        print(A)
        for j in range(i-1, -1, -1):
            if A[j] > A[j+1]:
                x = A[j]
                A[j] = A[j+1]
                A[j+1] = x
            else:
                break
    return A

