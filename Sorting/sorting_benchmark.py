from sorting import bubble_sort,selection_sort,insertion_sort,merge_sort
from time import time
from random import randint

def create_array(size=10,maximum=50):
    return [randint(0,maximum) for _ in range(size)]

n = [10,100,1000,10000]
times = {'Bubble':[], 'Selection':[],'Insertion':[],'Merge':[]}

for size in n:
    a = create_array(size=size,maximum=size)
    t0 = time()
    bubble_sort(a)
    t1 = time()
    times['Bubble'].append(t1-t0)

    a = create_array(size=size,maximum=size)
    t0 = time()
    selection_sort(a)
    t1 = time()
    times['Selection'].append(t1-t0)

    a = create_array(size=size,maximum=size)
    t0 = time()
    insertion_sort(a)
    t1 = time()
    times['Insertion'].append(t1-t0)

    a = create_array(size=size,maximum=size)
    t0 = time()
    merge_sort(a)
    t1 = time()
    times['Merge'].append(t1-t0)

print('n\tBubble\tSelection\tInsertion\tMerge')
print(50*'_')
for i, size in enumerate(n):
    print('%d\t%0.5f\t%0.5f \t%0.5f \t%0.5f'%(size,times['Bubble'][i],
    times['Selection'][i],times['Insertion'][i],times['Merge'][i]))

#TODO: Add quicksort