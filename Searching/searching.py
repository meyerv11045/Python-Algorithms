''' Linear Search O(n)
    Avg/Worst Case Performace: O(n)
    Best Case Performance (first element in array): O(1)
'''
def linear_search(n,arry):
    for i in range(len(arry)):
        if arry[i] == n:
            return i 
    return -1 

arry1 = [54, 36, 9, 14, 45, 24, 3, 76]
print(linear_search(14,arry1))
