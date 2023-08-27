


def letterCombinations(digits):
    if not digits:
        return []
    
    phone_vals = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"}
    res = []
    
    def addtores(combination, next_digits):
        if not next_digits:
            res.append(combination)
            return
        
        for letter in phone_vals[next_digits[0]]:
            addtores(combination + letter, next_digits[1:])
    
    addtores("", digits)
    return res

print(letterCombinations("23"))
