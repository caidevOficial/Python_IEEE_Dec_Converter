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


def get_decimal_input() -> str:
    """[summary]
    Gets the decimal input from the user.
    
    Returns:
        str: [The decimal input]
    """
    number = input('Enter a [Integer or Float number]: ')
    return number

def get_IEEE_754_string() -> str:
    """[summary]
    Gets a number in the input an convert it in a IEEE 754 string.
    Returns:
        str: [The IEEE754 string]
    """
    ieee_string = input('Enter a IEEE 754 Binary String: ')
    ieee_string = ieee_string.replace(' ', '')

    return ieee_string

def _get_option() -> str:
    """[summary]
    Gets the option from the user.
    Returns:
        str: [The option selected]
    """
    option = input('Select an option [Only the number]: ')
    return option

def print_menu() -> str:
    """[summary]
    Prints the menu with the options of the app.

    Returns:
        str: [The selected menu option]
    """
    print_message('_',
        'Here you can convert a number',
        'from decimal to IEEE 754 or',
        'from IEEE 754 to decimal.',
        '[1] - Decimal to IEEE 754',
        '[2] - IEEE 754 to Decimal',
    )
    return _get_option()

def print_message(symbol: str, *args) -> None:
    """[summary]
    Prints a message to the user.
    Args:
        *args: [The messages to print]
    """
    symbols = _generate_symbols(symbol, args)
    print(f'\n{symbols}')
    for arg in args:
        print(f'## {arg}')
    print(f'{symbols}\n')

def _generate_symbols(symbol: str, strings: list) -> str:
    """[summary]
    Generates a string with the given symbol.
    Args:
        symbol (str): [The symbol to use]
        strings (list): [The strings to use]
    Returns:
        str: [The generated string]
    """
    amount = _get_longest_string(strings)
    symbols = ''
    for _ in range(amount+3):
        symbols += symbol
    
    return symbols
    

def _get_longest_string(strings: list) -> int:
    """[summary]
    Gets the amount of characters of longest string in a list.

    Args:
        strings (list): [The list with the strings]

    Returns:
        int: [The amount of characters of longest string]
    """
    longest_string = 0
    for string in strings:
        if len(string) > longest_string:
            longest_string = len(string)
    return longest_string
