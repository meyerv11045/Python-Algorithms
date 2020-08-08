''' Linear Search O(n)
    Avg/Worst Case Performace: O(n)
    Best Case Performance (1st element in array): O(1)
'''
def linear_search(n,arry):
    for i in range(len(arry)):
        if arry[i] == n:
            return i 
    return -1 

''' Binary Search O(log n)
    Takes pre-sorted array as input
    Avg/Worst Case performance: O(log n)
    Best Case Performance (1st elem in array): O(1)
'''
def binary_search_iterative(arry,target):
    low = 0
    high = len(arry) - 1

    while low <= high:
        mid = (low + high) // 2 
        if target == arry[mid]: 
            return mid
        elif target < arry[mid]: 
            high = mid - 1
        else: 
            low = mid + 1
    return -1

def binary_search_recursive(arry,L,R,target):
    if R < L: return -1 #Entire array searched, element not found
    mid = (L + R) // 2
    if arry[mid] == target: return mid
    elif arry[mid] < target: return binary_search_recursive(arry,mid+1,R,target)
    else: return binary_search_recursive(arry,L,mid-1,target)
