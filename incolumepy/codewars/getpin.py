# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'

from itertools import combinations, permutations, product


neighbords = {
    0: ['8'],
    1: ['1', '2', '4'],
    2: ['1', '2', '3', '5'],
    3: ['2', '3', '6'],
    4: ['1', '4', '5', '7'],
    5: ['2', '4', '5', '6', '8'],
    6: ['3', '5', '6', '9'],
    7: ['4', '7', '8'],
    8: ['0', '5', '7', '8', '9'],
    9: ['6', '8', '9']}


def tratativa5(pin):
    """

    :param pin:
    :return:
    """
    assert int(pin), f'ValueError{pin}'
    ent = str(pin)
    result, temp = [], []
    if len(ent) <= 1:
        result += neighbords.get(int(pin))
    for i in ent:
        temp.append(i)
    return list(combinations([0, 1, 2], 1))
    # return sorted(result)


def tratativa1(pin: (int, str)) -> list:
    """

    :return:
    """
    print(list(combinations(pin, 2)))
    print(list(permutations(pin, 2)))


def tratativa2(pin):
    caracteres = [0, 1, 2]
    permsList = [''.join(str(i) for i in x) for x in product(caracteres, repeat=2)]
    print(permsList)  # ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    # ou se valores string
    permsList = [''.join(x) for x in product('012', repeat=2)]
    print(permsList)  # ['00', '01', '02', '10', '11', '12', '20', '21', '22']


def tratativa3(pin: (str, int)) -> list:
    pass
    assert int(pin), f'ValueError {pin}'
    ent = str(pin)
    result, temp = [], []
    for i in ent:
        temp.append(neighbords.get(int(i)))
    print(temp)


def tratativa4(pin: (str, int)) -> list:
    assert int(pin), f'ValuerError {pin}'
    ent = str(pin)
    result, temp = [], []
    temp = [neighbords.get(int(i)) for i in ent]
    result = list(product(*temp))
    print(result)
    print(list(result))
    print([''.join(x) for x in result])


def get_pins(pin: (int, str)) -> list:
    """

    :param pin:
    :return:
    """
    assert int(pin), f'ValuerError {pin}'
    ent = str(pin)
    result, temp = [], []
    if len(ent) <= 1:
        return neighbords.get(int(pin))
    temp = [neighbords.get(int(i)) for i in ent]
    result = list(product(*temp))
    return [''.join(x) for x in result]


def run():
    # print(get_pins(8))
    tratativa4('11')


if __name__ == '__main__':
    run()
