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
        int_set_pi = (abs(int_set_pi) + 2) * check_int_set_pi(int_set_pi)
    return round(4 * return_pi, len(str(imp)) - 1)

def check_int_set_pi(imp_int_set_pi):
    if imp_int_set_pi > 0:
        return -1
    else:
        return 1
