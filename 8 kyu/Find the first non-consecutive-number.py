def first_non_consecutive(arr):
    #your code here
    
    for i,j in enumerate(arr,arr[0]):
        if i !=j:
            return j
    None
