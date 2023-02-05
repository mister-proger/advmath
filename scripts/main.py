import supportlib

def multipliers(number, all = None, one = None):
    list_multipliers = []
    if all:
        for n in range(1, number + 1):
            if number % n == 0:
                list_multipliers.append(n)
        return list_multipliers
    else:
        n = 2
        while number != 1:
            if number % n == 0:
                list_multipliers.append(n)
                number = number // n
            else:
                n += 1
        if len(list_multipliers) == 1 and one:
            list_multipliers.insert(0, 1)
        return list_multipliers

def gcd(arg):
    if type(arg) == list:
        for n in range(len(arg)):
            arg.insert(n, multipliers(arg.pop(n), one = True))
        while arg[-2] != 1:
            for tag in range(len(arg) - 1):
                list_mul = []
                for a in range(len(arg[tag])):
                    for b in range(len(arg[tag + 1])):
                        if (arg[tag])[a] == (arg[tag + 1])[b]:
                            list_mul.append((arg[tag])[a])
                            (arg[tag])[a], (arg[tag + 1])[b] = 1, 1
                arg[tag], arg[tag + 1] = 1, list_mul
        return supportlib.mul(arg[-1])

def scm(arg, debug = False):
    for n in range(len(arg)):
        arg.insert(n, multipliers(arg.pop(n)))
        if debug:
            print('arg:', arg)
    while arg[-2] != 1:
        for tag in range(len(arg) - 1):
            list_mul = []
            if debug:
                print('tag:', tag, '| arg:', arg)
            for a in range(len(arg[tag])):
                for b in range(len(arg[tag + 1])):
                    if (arg[tag])[a] == (arg[tag + 1])[b]:
                        list_mul.append((arg[tag])[a])
                        (arg[tag])[a], (arg[tag + 1])[b] = 1, 1
                    if debug:
                        print('a:', a, '| b:', b, '| tag:', tag, '| arg:', arg, '| list_mul:', list_mul)
            arg[tag], arg[tag + 1] = 1, multipliers(supportlib.mul(arg[tag]) * supportlib.mul(arg[tag + 1]) * supportlib.mul(list_mul))
    return supportlib.mul(arg[-1])
