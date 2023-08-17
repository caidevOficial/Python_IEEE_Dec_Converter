# MIT License
# 
# Copyright (c) 2022 [FacuFalcone]
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
from tkinter.messagebox import showinfo as alert

def __positive_int_to_bin(number: int) -> str:
    """[summary]
    Bassed on a positive integer,\n
    returns the corresponding binary string.

    Args:
        number (int): [The positive integer to convert]

    Returns:
        str: [The corresponding binary string]
    """
    final_bin_string = __dec_to_simple_bin(abs(number))
    return final_bin_string

def __decimal_part_to_bin(number: str) -> str:
    """[summary]
    Gets the decimal part of a number and converts it into a binary string.
    
    Args:
        number (str): [The decimal part of the number]
        
    Returns:
        str: [The binary string of the decimal part]
    """
    dec_number = float(f'0.{number}')
    dec_bin = ''
    while dec_number < 1:
        dec_number *= 2
        dec_bin = f'{dec_bin}{int(dec_number)}'
    # dec_bin = np.binary_repr(int(number))
    return dec_bin

def __dec_to_simple_bin(dec_number: int):
    # bin_number = 0
    # multiplier = 1

    # while dec_number > 0:
    #     bin_number = bin_number + dec_number % 2 * multiplier
    #     dec_number //= 2
    #     multiplier *= 10
    bin_number = np.binary_repr(int(dec_number))
    return f'{bin_number}'

def __check_for_comma(number: str) -> bool:
    """
    The function checks if a given string contains a comma.
    
    :param number: The parameter "number" is a string that represents a number
    :return: a boolean value indicating whether a comma ('.') is present in the input string.
    """
    return '.' in number

def __binary_base_string(int_bin: str, dec_bin: str) -> str:
    """[summary]
    If the decimal part is not 0,\n
    concatenate the decimal part to the integer part with a '.'
    otherwise returns only the integer part.
    
    Args:
        int_bin (str): [The integer part of the number]
        dec_bin (str): [The decimal part of the number]
        
    Returns:
        str: [The final binary string]
    """
    if dec_bin == '0':
        return int_bin
    else:
        return f'{int_bin}.{dec_bin}'

def __get_exponent(integer_bin: str) -> int:
    """[summary]
    Gets how many places should move the comma 'till find a 1 to the left of the comma.

    Args:
        full_bin_number (str): [The full binary number]

    Returns:
        int: [The exponent]
    """
    exponent = 0
    places = 0
    for i in integer_bin:
        places += 1
        if i == '1':
            exponent = len(integer_bin) - places
            break
    return exponent

def __complete_mantisse(exponent: int, integer_binary: str, decimal_part_bin:str) -> str:
    """[summary]
    Complete with 0's to the right many times the mantisse[12] is not full.

    Args:
        exponent (int): [The exponent that indicates how many places the comma was moved]
        integer_binary (str): [The integer part of the number to take the digit that is after the comma]
        decimal_part_bin (str): [The decimal part of the number]

    Returns:
        str: [The mantisse]
    """
    mantisse = f'{integer_binary[len(integer_binary) - exponent:]}{decimal_part_bin}'
    while len(mantisse) < 23:
        mantisse = f'{mantisse}0'
    
    return mantisse

def get_report_dec_to_IEEE_754(number: str) -> None:
    """
    The function `get_report_dec_to_IEEE_754` converts a decimal number to its IEEE 754 representation
    and generates a report with the intermediate steps and the final result.
    
    :param number: The `number` parameter is a string representing a decimal number
    :type number: str
    """
    number: str = number.replace(',', '.')
    decimal_binary = '0'
    have_comma = __check_for_comma(number)
    if have_comma:
        numbers_sections = number.split('.')
        integer: str = numbers_sections[0]
        if len(numbers_sections) == 2:
            decimal_binary: str = __decimal_part_to_bin(numbers_sections[1])
    else:
        integer = number
    integer_binary: str = __positive_int_to_bin(int(integer))
    full_binary_base: str = f'{__binary_base_string(integer_binary, decimal_binary)}'
    
    exponent = __get_exponent(integer_binary)
    shifted_exp = exponent + 127
    shifted_bin_exp = __dec_to_simple_bin(shifted_exp)
    sign: str = '1' if integer[0] == '-' else '0'
    mantisse = __complete_mantisse(exponent, integer_binary, decimal_binary)
    final_IEEE754: str = f'{sign} {shifted_bin_exp} {mantisse}'

    if have_comma:
            cientific_notation = f'The Full Binary in cientific notation is: {full_binary_base}x2^{exponent}'
    else:
        cientific_notation = f'The Full Binary in cientific notation is: {full_binary_base}'

    #? ####### Messages to the user ########
    message =\
    f"""
    The Integer part to Binary is: {integer_binary}
    The Decimal part to Binary is: {decimal_binary}
    {cientific_notation}'
    The exponent in decimal is: {exponent}
    The exponent in binary is: {__dec_to_simple_bin(exponent)}
    The shifted exponent is: {shifted_exp}
    The shifted exponent in binary is: {shifted_bin_exp}'
    The Sign is: {sign}
    The shifted exponent in binary is: {shifted_bin_exp}
    The Mantisse is: {mantisse}
    The Final IEEE 754 String is:
    {final_IEEE754}
    """
    alert('IEEE 754 Report', message)

def dec_to_IEEE754(number: float | int) -> str:
    """
    The function `dec_to_IEEE754` converts a decimal number to its IEEE 754 representation.
    
    :param number: The number parameter is the decimal number that you want to convert to IEEE 754
    format. It can be either a float or an integer
    :type number: float | int
    :return: a string representation of the given number in IEEE 754 format.
    """
    import ieee754
    ieee_str = ieee754.IEEE754(
        number, precision=1, force_length=32, force_exponent=8, 
        force_mantissa=23)
    return f'{ieee_str.__str__()[0]} {ieee_str.__str__()[1:9]} {ieee_str.__str__()[9:]}'
