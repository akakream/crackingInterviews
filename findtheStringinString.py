import collections

small = 'abbc'
large = 'cbabadcbbabbcbabaabccbabc'


def findWithin(small, large):
    
    howmany = 0

    for i in range(len(large)-len(small)+1):
        window = large[i:i+4]
        if window[0] in small:
            
            if collections.Counter(window) == collections.Counter(small):
                howmany += 1

    return howmany

print(f"len(large): {len(large)}")

result = findWithin(small, large)
print(f"result: {result}")
