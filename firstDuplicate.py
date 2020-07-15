
# THe numbers in array must be between 0 and len(array)

test1 = [1,2,1,2,3,3] # answer is 1
test2 = [2,1,3,5,3,2] # answer is 3
test3 = [1,2,3,4,5,6] # answer is -1

# Time Complexity is O(n)

def findFirstDuplicate(array):
    hashmap = {}

    # O(n) loop through array
    for el in array:
       
        # O(1) for lookup
        if el not in hashmap:
            hashmap[el] = 1
        
        else:
            hashmap[el] = hashmap[el] + 1
       
        if hashmap[el] == 2:
            return el


    return -1

# Time Complexity is O(n)

def findWithHashSet(array):
    hashset = set()

    for el in array:

        if el in hashset:
            return el
        else:
            hashset.add(el)

    return -1

# These have a Space Complexity of O(n), because of the hash map and set
# Lets find a better one with O(1), both space and time

def bestFind(array):

    for el in array:

        if array[abs(el)-1] < 0:
            return abs(el)
        
        array[abs(el)-1] = - array[abs(el)-1]

    return -1


'''
ans1 = findFirstDuplicate(test1)
ans2 = findFirstDuplicate(test2)
ans3 = findFirstDuplicate(test3)

print(f"ans1: {ans1}")
print(f"ans2: {ans2}")
print(f"ans3: {ans3}")

ans1 = findWithHashSet(test1)
ans2 = findWithHashSet(test2)
ans3 = findWithHashSet(test3)

print(f"ans1: {ans1}")
print(f"ans2: {ans2}")
print(f"ans3: {ans3}")
'''

ans1 = bestFind(test1)
ans2 = bestFind(test2)
ans3 = bestFind(test3)

print(f"ans1: {ans1}")
print(f"ans2: {ans2}")
print(f"ans3: {ans3}")
