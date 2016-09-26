#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Bit manipulation module
"""
__version__ = "1.0.0"
__author__ = "Qu DoNG"

BIT0 = 1 << 0
BIT1 = 1 << 1
BIT2 = 1 << 2
BIT3 = 1 << 3
BIT4 = 1 << 4
BIT5 = 1 << 5
BIT6 = 1 << 6
BIT7 = 1 << 7
BIT8 = 1 << 8
BIT9 = 1 << 9
BIT10 = 1 << 10
BIT11 = 1 << 11
BIT12 = 1 << 12
BIT13 = 1 << 13
BIT14 = 1 << 14
BIT15 = 1 << 15

if 1:  # a bit more efficient in this case
    BIT = {0: 1,
           1: 2,
           2: 4,
           3: 8,
           4: 16,
           5: 32,
           6: 64,
           7: 128,
           8: 256,
           9: 512,
           10: 1024,
           11: 2048,
           12: 4096,
           13: 8192,
           14: 16384,
           15: 32768}
else:
    BIT = {}
    for i in range(32): BIT[i] = (1 << i)


class BitsError(Exception):
    pass


def gen_mask_shift(*args):
    """
    For instance, I want to set bit2, bit3, bit4
    bit 7654 3210
    0b  0001 1100

    So the generated mask result is 0x1C, the shift bit is 2.

    > mask, shift = gen_mask_shift(2,3,4)
    > print(hex(mask), shift)

    :param args: The bits you'd like to set
    :return: a tuple which the first para is the mask result, and the second para is the number of bits to be shifted
    """
    mask = 0
    shift = min(args)
    for i in args:
        mask |= BIT[i]
    return mask, shift


def lowestSet(int_type):
    """
    Find the lowest SET bit in an integer, for instance, 0b1100 => 2

    :param int_type: a Python integer type
    :return:
    """
    low = (int_type & -int_type)
    lowBit = -1
    while (low):
        low >>= 1
        lowBit += 1
    return lowBit


def set_bits_uint8_reg_val(reg_val, val, *args):
    """
    Set certain bits of a register value with a set-value, you will need to pass the bits you'd like to set at least,
    or pass an extra parameter which is the number of shift need to performed for the task

    :param reg_val: the value you'd like to change
    :param val: the new set value, Note this value should be smaller than (mask+1)
    :param args: [mask, shift] or just [mask]
    :return: the new reg_val with [mask] bits are set as the val
    """
    argslen = len(args)
    # print(argslen)
    if argslen == 2:
        mask, shift = args
    elif argslen == 1:
        mask = args[0]
        shift = lowestSet(mask)
    else:
        raise BitsError("Passed args val should be [mask, shift] or [mask]")
    reg_val &= (~ mask)
    if val:
        return reg_val | (val << shift)
    else:
        return reg_val


def get_bits_uint8_reg_val(reg_val, *args):
    """
    args = [mask, shift] or [mask]

    :param reg_val:
    :param args:
    :return:
    """
    argslen = len(args)
    # print(argslen)
    if argslen == 2:
        mask, shift = args
    elif argslen == 1:
        mask = args[0]
        shift = lowestSet(mask)
    else:
        raise BitsError("Passed args val should be [mask, shift] or [mask]")
    return (reg_val & mask) >> shift


def get_bit_uint8(reg_val, bit):
    """
    Get a Single bit of a Python integer;

    :param reg_val: a python integer
    :param bit: the bit you are interested
    :return:
    """
    # todo-qd: actually instead of using bit shift, I could just use a hash table
    return (reg_val & (1 << bit)) >> (bit)


def set_bit_uint8(reg_val, bit, set_val):
    """
    Set a Single bit of a Python integer

    :param reg_val:
    :param bit:
    :param set_val:
    :return:
    """
    return (reg_val & ~(1 << bit)) | (set_val << bit)


if __name__ == "__main__":
    # For instance, I'd like to set bit 5 and bit 6
    #               ..
    # original: 0b 0011 1111
    # expected: 0b 0111 1111
    reg = 0x3f
    val = 3  # 0b11
    mask_shift = gen_mask_shift(5, 6)
    # print(mask_shift)

    rslt = set_bits_uint8_reg_val(reg, val, *mask_shift)
    print('Output [expected: 0x7f] is ', hex(rslt))

    print('Mask is {0:#x}; Shift is {1}'.format(mask_shift[0], mask_shift[1]))
    print('Get the bits set just now: {}\n'.format(get_bits_uint8_reg_val(rslt, *mask_shift)))

    ####################################################################
    mask_shift = gen_mask_shift(1, 2, 3)
    rslt = set_bits_uint8_reg_val(reg, 0b101, *mask_shift)
    print('[Method 1 - Preferred] Output [expected: 0x3b] is ', hex(rslt))
    rslt = set_bits_uint8_reg_val(reg, 0b101,
                                  BIT1 | BIT2 | BIT3)  # another way of using this, but timing complexity is longer
    print('[Method 2] Output [expected: 0x3b] is ', hex(rslt))

    print('Expected value is 0x20: ', hex(set_bit_uint8(0x00, 5, 1)))
    print('Expected value is 0xf0: ', hex(set_bit_uint8(0xf0, 3, 0)))

    mask, shift = gen_mask_shift(2, 3, 4)
    print('If Bit 2, 3, 4 are set, the expected mask value is 0x1c and the bits to be shifted is 2: ', hex(mask), shift)

    a = 0b1100
    print('lowest set bit for {0:x} is {1}'.format(a, lowestSet(a)))
    print('lowest set bit for {0:#X} is {1}'.format(a, lowestSet(a)))
    pass
