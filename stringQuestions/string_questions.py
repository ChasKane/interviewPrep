def print_dups(s):
    result = ""
    if not s: return result
    alpha = ""
    for c in s:
        if c in alpha:
            result += c
        else:
            alpha += c

    return result
