import random
import numpy as np
from timer import timer
from heap_tree import Heaptree

def bubble_sort(nLst):
    length = len(nLst)
    for i in range(length-1):
        for j in range(length-1-i):
            if nLst[j] > nLst[j+1]:
                nLst[j],nLst[j+1] = nLst[j+1],nLst[j]
    return nLst

def cocktail_sort(nLst):
    n = len(nLst) 
    is_sorted = True
    start = 0                                       
    end = n-1                                      
    while is_sorted: 
        is_sorted = False                           
        for i in range (start, end):                
            if (nLst[i] > nLst[i + 1]) : 
                nLst[i], nLst[i + 1]= nLst[i + 1], nLst[i] 
                is_sorted = True
        if not is_sorted:
            break

        end = end-1  
        for i in range(end-1, start-1, -1):
            if (nLst[i] > nLst[i + 1]): 
                nLst[i], nLst[i + 1] = nLst[i + 1], nLst[i] 
                is_sorted = True
        start = start + 1 
    return nLst

def selection_sort(nLst):
    for i in range(len(nLst)-1):        
        index = i
        for j in range(i+1, len(nLst)):
            if nLst[index] > nLst[j]:
                index = j
        if i == index:
            pass
        else:
            nLst[i],nLst[index] = nLst[index],nLst[i]
    return nLst

def insertion_sort(nLst):
    n = len(nLst)
    if n == 1:
        return nLst
    for i in range(1,n):
        for j in range(i, 0, -1):
            if nLst[j] < nLst[j-1]: 
                nLst[j], nLst[j-1] = nLst[j-1], nLst[j]
            else:
                break
    return nLst

def quick_sort(nLst):
    if len(nLst) <= 1:
        return nLst

    left = []
    right= []
    piv = []
    pivot = random.choice(nLst)
    for val in nLst:
        if val == pivot:
            piv.append(val)
        elif val < pivot:
            left.append(val)
        else:
            right.append(val)
    return quick_sort(left) + piv + quick_sort(right)

def merge(left, right):
    output = []
    while left and right:
        if left[0] <= right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    if left:
        output += left
    if right:
        output += right
    return output

def merge_sort(nLst):
    if len(nLst) <= 1:
        return nLst    
    mid = len(nLst) // 2             
    left = nLst[:mid]
    right = nLst[mid:]                      
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

if __name__ == '__main__':
    h = list(np.random.randint(0, 100, 10))
    print("Data Before Sort : ", h)
    print("=============")
    print("Bubble Sort Result : ", bubble_sort(h))
    print("Bubble Sort Time Consumption : ", timer(bubble_sort, h, rep= 10000))
    print("=============")
    print("Cocktail Sort Result : ", cocktail_sort(h))
    print("Cocktail Sort Time Consumption : ", timer(cocktail_sort, h, rep= 10000))    
    print("=============")
    print("Selection Sort Result : ", selection_sort(h))
    print("Selection Sort Time Consumption : ", timer(selection_sort, h, rep= 10000))    
    print("=============")    
    print("Insertion Sort Result : ", insertion_sort(h))
    print("Insertion Sort Time Consumption : ", timer(insertion_sort, h, rep= 10000))    
    print("=============")    
    print("Quick Sort Result : ", quick_sort(h))
    print("Quick Sort Time Consumption : ", timer(quick_sort, h, rep= 10000))    
    print("=============")        
    print("Merge Sort Result : ", merge_sort(h))
    print("Merge Sort Time Consumption : ", timer(merge_sort, h, rep= 10000))             
    print("=============")
    obj = Heaptree()
    obj.build_heap(h)
    obj.heap_sort()
    new_obj = Heaptree()
    print("Heap Sort Time Consumption : Build Heap", timer(new_obj.build_heap, h, rep= 10000))        
    print("Heap Sort Time Consumption : Heap Sort", timer(new_obj.heap_sort, rep= 10000)) 
    print("Heap Sort Result : ", obj.sort_data)
    
    
    
    
    
    