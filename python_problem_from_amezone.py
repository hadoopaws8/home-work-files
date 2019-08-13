def first_recurring(given_string):
    counts={}
    for char in given_string:
        if char in counts:
            return char
        counts[char]=1
       # print(counts)
    return None

st=first_recurring("DBCABA")
print(st)
