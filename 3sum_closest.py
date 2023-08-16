def find_closest(arr,target):
    l = []
    diffs = []
    for i in range(len(arr)-1):
        for k in range(i+1,len(arr)-1):
            for m in arr[k+1:]:
                l.append(arr[i]+ arr[k] + m)
    
    for i in range(len(l)):
        diffs.append(abs(l[i]-target))
    
    smallest = min(diffs)
    val_index = diffs.index(smallest)
    return l[val_index]

nums = [-1,2,1,-4]
print(find_closest(nums,4))

