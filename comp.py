from arithm import power, mult_div, add_subtr


def computing(lst):
    """
    Take the list with string items, find the math operations signs
    in it, call respective functions to execute this operations and
    return result as a string
    """
    if '^' in lst:
        lst = power(lst)
        if lst == 'Error: unexpected value':            
            return lst

    if '*' in lst or '/' in lst:
        lst = mult_div(lst)
        if lst == 'Error: division by zero':
            return lst

    if '+' in lst or '-' in lst:
        lst = add_subtr(lst)

    string_result = str(lst[0])
    return string_result

