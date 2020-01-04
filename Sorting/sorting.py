from random import randint

''' Bubble Sort O(n^2)
    Avg/Worst Case Performace: O(n^2) comparisons & swaps
    Best Case Performance (presorted array): O(n) comparisons & O(1) swaps 
'''
def bubble_sort(arry):
    m = len(arry)
    for i in range(m):
        for j in range(0,m-i-1):
            if arry[j] > arry[j+1]:
                arry[j],arry[j+1] = arry[j+1],arry[j]

def bubble_sort_opt(arry):
    m = len(arry)
    for i in range(m):
        swapped = False
        for j in range(0,m-i-1):
            if arry[j] > arry[j+1]:
                arry[j],arry[j+1] = arry[j+1],arry[j]
                swapped = True
        if not swapped: #Handles pre-sorted arrys in O(n)
            break 

''' Selection Sort O(n^2)
    Avg/Worst/Best Case Performace: O(n^2)
    Makes O(n) swaps (the min amongst all sorting algos)
'''
def selection_sort(arry):
    m = len(arry)

    for i in range(m):
        smallest_index = i

        for j in range(i+1,m):
            if arry[j] < arry[smallest_index]:
                smallest_index = j

        arry[i],arry[smallest_index] = arry[smallest_index], arry[i]

''' Insertion Sort O(n^2)
    Avg/Worst Case Performance: O(n^2) comparisons & swaps
    Best Case Performance: O(n) comparisons & O(1) swaps
'''
def insertion_sort(arry):
    for i in range(1,len(arry)):
        val_to_sort = arry[i]
        j = i

        while j > 0 and arry[j-1] > val_to_sort:
            arry[j],arry[j-1] = arry[j-1],arry[j]
            j -= 1

''' Merge Sort O(n log n)
    Best/Avg/Worst Case Performance: O(n log n)
'''
def merge(arryA,arryB):
    c = []
    a_idx, b_idx = 0,0
    while a_idx < len(arryA) and b_idx < len(arryB):
        if arryA[a_idx] < arryB[b_idx]:
            c.append(arryA[a_idx])
            a_idx += 1
        else:
            c.append(arryB[b_idx])
            b_idx += 1

    #Add the remaining presorted elements to the end of array c
    if a_idx == len(arryA): 
        c.extend(arryB[b_idx:])
    else:
        c.extend(arryA[a_idx:])
    return c

def merge_sort(arry):
    if len(arry) <= 1:
        return arry
    left,right = merge_sort(arry[:len(arry)//2]), merge_sort(arry[len(arry)//2:]) #Splitting Routine O(log n)
    return merge(left,right) #Merging routine O(n)

'''Quicksort O(n log n)
    Best/Avg Case Performance: O(n log n)
    Worst Case Performance (pivots are maxs/mins of arry): O(n^2)
'''
def quicksort(arry):
    if len(arry) <= 1: return arry
    smaller, equal, larger = [],[],[]
    pivot = arry[randint(0,len(arry)-1)] #choosing a random pivot helps avoid the worst case performance
    for x in arry:
        if x < pivot: smaller.append(x)
        elif x == pivot: equal.append(x)
        else: larger.append(x)
    return quicksort(smaller) + equal + quicksort(larger)