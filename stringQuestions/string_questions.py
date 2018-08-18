# I've omitted input validation since
# these would all have similar validation requirements.
# comments on runtimes are worst case unless specified.
def print_dups(s):
    # wonder if there's a way to do this without `seen`...
    # not super important, as runtime is O(n^2): n=len(s)
    # for x in s:
    #   seen = False
    #   for y in s:
    #       if x == y:
    #           if seen: print(y)
    #           else: seen = True;
    #
    # below runtime is O(1), since len(alpha)<=26
    result = ""
    alpha = ""
    for c in s:
        if c in alpha:
            result += c
        else:
            alpha += c
    return result

def is_anagram(s1, s2):
    # lol potentailly infinite runtime if shuffle() is random
    # while True:
    #   if s1.shuffle() == s2: return True

    # heh, even better, as it's one line and clever, but
    # we must assume (due to sorting) that it's O(n log n): n=max(len(s1), len(s2))
    # return sorted(s1) == sorted(s2)

    # below runtime is O(n): n=max(len(s1), len(s2))
    if len(s1) != len(s2): return False
    letterCounts1 = {}
    letterCounts2 = {}
    for c1, c2 in zip(s1, s2):
        if c1 in letterCounts1: letterCounts1[c1] += 1
        else: letterCounts1[c1] = 1
        if c2 in letterCounts2: letterCounts2[c2] += 1
        else: letterCounts2[c2] = 1
    return letterCounts1 == letterCounts2

def first_nonrepeated_character(s):
    letterCounts = {}
    for c in s:
        if c in letterCounts: letterCounts[c] += 1
        else: letterCounts[c] = 1
    for c in s:
        if letterCounts[c] == 1: return c
    return ""

def recursive_string_reverse(s):
    # lol return s[::-1]
    if len(s) < 2:
        return s
    # put last char first, put the reversed
    # version of the rest of the string after it
    return s[-1:] + recursive_string_reverse(s[:-1])
