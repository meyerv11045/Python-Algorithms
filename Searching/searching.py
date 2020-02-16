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
def binary_search_iterative(n,arry):
    low = 0
    high = len(arry) - 1

    while low <= high:
        mid = (low + high) // 2 
        if n == arry[mid]: 
            return mid
        elif n < arry[mid]: 
            high = mid - 1
        else: 
            low = mid + 1
    return -1

def binary_search_recursive(n,arry,low,high):
    if low > high: return -1 #Base case
    mid =(low + high) // 2
    if n == arry[mid]: 
        return mid
    elif n < arry[mid]: 
        return binary_search_recursive(n,arry,low,mid-1)
    else: 
        return binary_search_recursive(n,arry,mid+1,high)