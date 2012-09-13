#coding: utf-8


def partition(array, pivot):
    new_pivot = reduce(lambda a, b: a + (b < array[pivot]), array, 0)

    array[pivot], array[new_pivot] = array[new_pivot], array[pivot]

    j=len(array)-1    
    for i in range(0, new_pivot):
        if array[i] >= array[new_pivot]:
            while array[j] >= array[new_pivot]:
                j-=1
            array[i], array[j] = array[j], array[i]
                
    return new_pivot
