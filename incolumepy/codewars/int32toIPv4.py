# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'


def tratativa(int32: int):
    num = f'{int32:#b}'[2:]
    num = f'{num:0>32}'
    print(f'{int32} : {num} : {len(num)}')
    ip = []
    ii = 0
    il = ii + 8
    try:
        # ip.append(num[ii:il])
        print(len(num[2:]), num[2:])
        print(len(num[2:]) % 8)
        print(num[26:34])
        print(num[34:])
        while ii < len(num) - 2:
            ip.append(num[ii:il])
            ii += 8
            il += 8
    except:
        raise

    print(
        num,
        ip,
        len(ip[0]),
        '.'.join([f"{int(x, 2)}" for x in ip])
    )


def int32_to_ip(int32: int):
    num = f'{int32:#b}'[2:]
    num = f'{num:0>32}'
    ip = num[:8], num[8: 16], num[16: 24], num[24:]
    print(len(num), num, ip)
    return '.'.join([f"{int(x, 2)}" for x in ip])


if __name__ == '__main__':
    # print(int32_to_ip(2149583361))
    # print(int32_to_ip(2154959208))
    # print(tratativa(0))
    # print(tratativa(1820103483))
    int32_to_ip(1820103483)
