test1 = 'abcd'

def findPerms(string):

    if len(string) == 1:
        return list(string)

    s1 = string[:-1]
    
    returned = findPerms(s1)
    
    s2 = string[-1]

    willreturned = []

    for el in returned:
        for index in range(len(el)+1):
            will_inserted = list(el)
            will_inserted.insert(index, s2)
            will_inserted_string = ''.join(will_inserted)
            willreturned.append(will_inserted_string)
    
    return willreturned


result = findPerms(test1)

print(f"result: {result}")
print(f"len(result): {len(result)}")
