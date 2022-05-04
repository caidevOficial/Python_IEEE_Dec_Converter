
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
    print('\n__________________________')
    print('Here you can convert a number\nfrom decimal to IEEE 754 or\nfrom IEEE 754 to decimal.')
    print('[1] - Decimal to IEEE 754')
    print('[2] - IEEE 754 to Decimal')
    print('__________________________')
    return _get_option()

def print_message(*args) -> None:
    """[summary]
    Prints a message to the user.
    Args:
        *args: [The messages to print]
    """
    symbols = _generate_symbols('#', args)
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
