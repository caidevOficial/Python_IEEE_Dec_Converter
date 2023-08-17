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

def input_bin_ieee(bin_ieee_str: str) -> float:
    """[summary]
    Gets a binary string in IEEE 754 format and\n
    returns the corresponding float or int number.
    Args:
        bin_ieee_str (str): [The binary IEEE754 string]

    Returns:
        float: [The corresponding parsed number]
    """
    final_val = ''
    # Get the sign
    sign = bin_ieee_str[0]
    print(f'Sign: {sign}')
    # Get the exponent
    exp = bin_ieee_str[1:9]
    print(f'Actual Exponent: {exp}')
    shifted_exp = int(exp, 2)
    print(f'Shifted Exponent: {shifted_exp}')
    real_exponent = shifted_exp - 127
    print(f'Real Exponent: {real_exponent}')
    # Get the mantissa
    mant = bin_ieee_str[9:]
    print(f'Mantissa: {mant}')
    # Get the exponent value
    real_mant = mant[0:real_exponent]
    print(f'Real Mantissa: {real_mant}')
    final_number = f'{sign}{real_mant}'
    print(f'Final Binary Number: {final_number}')
    final_val = -1 * int(final_number, 2) if sign == '1' else int(final_number, 2)
    # Return the final value
    return final_val

if __name__ == '__main__':
    # Get the input
    bin_ieee_str = input('Enter a binary IEEE754 string: ')
    # Get the final value
    final_val = input_bin_ieee(bin_ieee_str)
    # Print the final value
    print(f'The IEEE 745 is: {bin_ieee_str}')
    print(f'The corresponding number is: {final_val}')