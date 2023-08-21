def sort_nums(s):
    """sorts s including decimals in ascending order."""
    dict_v = {'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
    sorted_s = ""
    
    for i in s:
        dict_v[i].append(i) # if we write dict_v[i] = i, there won't be any duplicates.
        
    for i in range(9):
        if dict_v[str(i)]:
            for i in dict_v[str(i)]:
                sorted_s +=i
                
    return sorted_s

sample = "241333"
print(sort_nums(sample))

