def mul(*args):
    if type(list(args)[0]) == list:
        return_number = 1
        for n in range(len(list(args)[0])):
            return_number *= list(args)[0][n]
        return return_number
    for n in range(len(list(args))):
        if not type(list(args)[n]) == int:
            print('Ошибка: аргумент ', str(list(args)[n]), 'не является числом.')
            return None
    return_number = 1
    for n in range(len(list(args))):
        return_number *= list(args)[n]
    return return_number

def sum(*args):
    if type(list(args)[0]) == list:
        return_number = 0
        for n in range(len(list(args)[0])):
            return_number += list(args)[0][n]
        return return_number
    for n in range(len(list(args))):
        if not type(list(args)[n]) == int:
            print('Ошибка: аргумент ', str(list(args)[n]), 'не является числом.')
            return None
    return_number = 0
    for n in range(len(list(args))):
        return_number += list(args)[n]
    return return_number

def multipliers(number, **kwargs):
    if not number:
        print('Ошибка: ожидалось число аргументов больше 0')
        return None
    list_multipliers = []
    if kwargs.get('all', False):
        for n in range(1, number + 1):
            if number % n == 0:
                list_multipliers.append(n)
                number //= n
        return list_multipliers
    else:
        n = 2
        while number != 1:
            if number % n == 0:
                list_multipliers.append(n)
                number = number // n
            else:
                n += 1
    if kwargs.get('one', False):
        list_multipliers.insert(0, 1)
    return list_multipliers

def factorial(number):
    return_number = 1
    for n in range(1, number + 1):
        return_number *= n
    return return_number

def dablfactorial(number):
    return_number = 1
    if number % 2 == 0:
        for n in range(2, number + 1, 2):
            return_number *= n
        return return_number
    else:
        for n in range(1, number + 1, 2):
            return_number *= n
        return return_number

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
        return mul(arg[-1])

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
            arg[tag], arg[tag + 1] = 1, multipliers(mul(arg[tag]) * mul(arg[tag + 1]) * mul(list_mul))
    return mul(arg[-1])
