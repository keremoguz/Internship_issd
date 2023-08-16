def find_comb(s):
    """
    finds all possible combinations and returns as a list
    """
    lists = []
    res = []
    val_dict = {'2':['a','b','c'], '3': ['d','e','f'],
                '4': ['g','h','i'], '5':['j','k','l'],
                '6': ['m','n','o'], '7': ['p','q','r','s'],
                '8': ['t','u','v'], '9': ['w','x','y','z']
                }
    if len(s)== 1:
        return [s]
    for i in s:
        lists.append(val_dict[i])
    for i in range(len(lists)):
        for k in range(len(lists[i])):
            for m in range(i+1,len(lists)):
                for n in lists[m]:
                    res.append(lists[i][k] + n)

    return res

print(find_comb("23"))





        

            


