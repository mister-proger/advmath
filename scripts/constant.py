import multipliers

def pi(*imp):
    if not imp:
        imp = 4
    else:
        imp = imp[0]
    rel_imp = '1'
    for n in range(imp + 1):
        rel_imp = rel_imp + '0'
    imp = int(rel_imp)
    del rel_imp
    return_pi = 0
    int_set_pi = 1
    for n in range(imp):
        return_pi += 1 / int_set_pi
        if int_set_pi > 0:
            int_set_pi = (int_set_pi + 2) * -1
        else:
            int_set_pi = (int_set_pi - 2) * -1
    return round(4 * return_pi, len(str(imp)) - 2)

def tau(*imp):
    if not imp:
        imp = 4
    else:
        imp = imp[0]
    return round(pi(imp), imp)

def e(*imp):
    if not imp:
        imp = 50
    else:
        imp = imp[0]
    return_e = 0
    for n in range(imp):
        return_e = return_e + 1 / supportlib.factorial(n)
    return round(return_e, imp)
