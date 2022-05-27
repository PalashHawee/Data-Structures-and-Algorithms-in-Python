#First Duplicate Value
# Time O(n) | Space(n)

def firstDuplicateValue(array):
    # Write your code here.
    seen=set()
    for value in array:
        if value in seen:
            return value
        seen.add(value)
    return -1    
    