'''
1.It is a time complexity of O(N^2)
2.It is also a comparison based sorting
3.it is an inplace sorting (doesnt need an extra memory)
4.it is not a stable sorting
'''
def Selection_sort(arr):
    for i in range(len(arr)-1):
        pointer=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[pointer]: #in ascending order (for descending order change it to < to  > sign)
                pointer=j

        if pointer != i:
            arr[i],arr[pointer]=arr[pointer],arr[i]  #swapping

    return (' '.join(arr))

ls=list(map(str,input('enter the array:').split()))
print(Selection_sort(ls))
