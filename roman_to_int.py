def roman_to_int(s):
    """Takes a string(s) including roman numbers 
        and returns the integer version of it
    """
    result = 0
    val_dict = {'I':1, 'V': 5, 'X' : 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    for i in range(len(s)-1):
        first_val = val_dict[s[i]]
        sec_val = val_dict[s[i+1]]

        if first_val< sec_val :
            result -= first_val
        else:
            result += first_val

    return result + val_dict[s[-1]] 

