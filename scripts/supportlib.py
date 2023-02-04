def mul(list_of_numbers):
    return_number = 1
    for n in range(len(list_of_numbers)):
        return_number = return_number * int(list_of_numbers[n])
    return return_number
