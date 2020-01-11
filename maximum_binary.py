def binary(number):
    if number//2 == 0:
        return str(number%2)
    else:
        return str(binary(number//2)) + str(number%2)

def max_binary(bit):
    array_of_binary = []
    for i in range(2**bit):
        binarys = binary(i)
        if len(list(binarys)) < bit:
            more_0 = "0" * (bit-len(list(binarys)))
            more_0 += binarys
            array_of_binary.append(more_0)
        else:
            array_of_binary.append(binarys)
    return array_of_binary