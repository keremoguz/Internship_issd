def find_comb(s):
    lists = []
    res = []
    val_dict = {'2':['a','b','c'], '3': ['d','e','f'],
                '4': ['g','h','i'], '5':['j','k','l'],
                '6': ['m','n','o'], '7': ['p','q','r','s'],
                '8': ['t','u','v'], '9': ['w','x','y','z']
                }
    for i in s:
        lists.append(val_dict[i])
    for i in range(len(lists)):
        for k in range(len(lists[i])):
            for m in range(i+1, len(lists)):  # Adjusted the range here
                for n in lists[m]:
                    res.append(lists[i][k] + n)

    return res

input_string = "237"
combinations = find_comb(input_string)
print(combinations)
