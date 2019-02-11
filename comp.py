from arithm import power, mult_div, add_subtr


def computing(lst):
    if '^' in lst:
        lst = power(lst)
        if lst is None:
            return

    if '*' in lst or '/' in lst:
        lst = mult_div(lst)
        if lst is None:
            return

    if '+' in lst or '-' in lst:
        lst = add_subtr(lst)

    string_result = str(lst[0])
    return string_result
