# GNU General Public License V3
#
# Copyright (C) 2023 <FacuFalcone>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math

def __get_integer_from_mantisse(mantisse: str, exponent: int) -> int:
    """
    The function takes a binary mantissa and exponent as input and returns the corresponding integer
    value.
    
    :param mantisse: The mantisse is a string representing the fractional part of a binary number. It
    consists of a sequence of binary digits (0s and 1s)
    :type mantisse: str
    :param exponent: The exponent parameter is an integer that represents the number of bits to consider
    from the mantisse parameter
    :type exponent: int
    :return: an integer value.
    """
    integer_part = f'1{mantisse[0:exponent]}'
    return int(integer_part, 2)

def __get_decimal_from_mantisse(sign: str, mantisse: str, exponent: int):
    """
    The function calculates the decimal value represented by the mantisse of a binary number given the
    sign, mantisse, and exponent.
    
    :param sign: The sign parameter is a string that represents the sign of the number. It can be either
    "+" or "-"
    :type sign: str
    :param mantisse: The mantisse is a string representing the fractional part of a binary number. It
    consists of a sequence of 0s and 1s
    :type mantisse: str
    :param exponent: The exponent is an integer that represents the power of 2 by which the mantissa
    should be multiplied
    :type exponent: int
    :return: the decimal value represented by the mantisse, given the sign, mantisse, and exponent.
    """
    dec_part = mantisse[exponent:]
    dec_part_sum = 0
    for i in range(len(dec_part)):
        if dec_part[i] == '1':
            dec_part_sum += int(dec_part[i]) * math.pow(2, -(i+1))
    return dec_part_sum

def __get_sign(sign: str) -> int:
    """
    The function returns 1 if the input sign is '0', otherwise it returns -1.
    
    :param sign: The parameter `sign` is a string that represents a sign. It can be either '0' or 1
    :type sign: str
    :return: an integer value between 1 or -1.
    """
    return 1 if sign == '0' else -1

def __get_float_number_from_mantisse(sign: str, exponent: int, mantisse: str):
    """
    The function takes in a sign, exponent, and mantisse and returns a float number.
    
    :param sign: The sign parameter is a string that represents the sign of the number. It can be either
    "+" or "-"
    :type sign: str
    :param exponent: The exponent is an integer value that represents the power of 10 by which the
    mantissa should be multiplied
    :type exponent: int
    :param mantisse: The mantisse parameter is a string that represents the mantissa of a floating-point
    number
    :type mantisse: str
    :return: a float number.
    """
    float_str = __get_sign(sign) * (
        __get_integer_from_mantisse(mantisse, exponent) +
        __get_decimal_from_mantisse(sign, mantisse, exponent)
    )
    return float(float_str)

def IEEE754_to_dec(binary_chain: str) -> str:
    """
    The function `IEEE754_to_dec` converts a binary representation of a floating-point number in IEEE
    754 format to its decimal equivalent.
    
    :param binary_chain: The `binary_chain` parameter is a string representing a binary number in IEEE
    754 format
    :type binary_chain: str
    :return: a string representation of the decimal number converted from the given IEEE 754 binary
    chain.
    """
    exponent = int(binary_chain[1:9], 2) - 127
    float_number = __get_float_number_from_mantisse(
        binary_chain[0], exponent, binary_chain[9:])
    return float_number
