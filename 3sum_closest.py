def find_closest(arr,target):
    l = []
    diffs = []
    for i in range(len(arr)-2):
        """ i th loop keeps track of the i th element to be summed."""
        for k in range(i+1,len(arr)-1):
            for m in arr[k+1:]:
                l.append(arr[i]+ arr[k] + m) # to store the sums, appends the sums to the list l.
    
    for i in range(len(l)):
        """appends the absolute differences between 
            target and sums to the diffs list """
        diffs.append(abs(l[i]-target))
    
    smallest = min(diffs) #finds the minimum difference
    val_index = diffs.index(smallest) # assigns index of the min difference to val_index
    return l[val_index]

nums = [-1,2,1,-4]
print(find_closest(nums,4))

