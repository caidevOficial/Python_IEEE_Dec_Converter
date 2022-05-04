
from Auxiliar_Mod.auxiliars import print_message as message

def positive_int_to_bin(number: int) -> str:
    """[summary]
    Bassed on a positive integer,\n
    returns the corresponding binary string.

    Args:
        number (int): [The positive integer to convert]

    Returns:
        str: [The corresponding binary string]
    """
    final_bin_string = _dec_to_simple_bin(abs(number))
    return final_bin_string

def decimal_part_to_bin(number: str) -> str:
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
    
    return dec_bin

def _dec_to_simple_bin(dec_number: int):
    bin_number = 0
    multiplier = 1

    while dec_number > 0:
        bin_number = bin_number + dec_number % 2 * multiplier
        dec_number //= 2
        multiplier *= 10

    return f'{bin_number}'

def check_for_comma(number: str) -> bool:

    if '.' in number:
        return True
    return False

def binary_base_string(int_bin: str, dec_bin: str) -> str:
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

def get_exponent(integer_bin: str) -> int:
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

def complete_mantisse(exponent: int, integer_binary: str, decimal_part_bin:str) -> str:
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

def dec_to_IEEE_754(number: str) -> None:
    number: str = number.replace(',', '.')
    decimal_binary = '0'
    have_comma = False
    if check_for_comma(number):
        have_comma = True
        numbers_sections = number.split('.')
        integer: str = numbers_sections[0]
        if len(numbers_sections) == 2:
            decimal_binary: str = decimal_part_to_bin(numbers_sections[1])
    else:
        integer = number
    integer_binary: str = positive_int_to_bin(int(integer))
    full_binary_base: str = f'{binary_base_string(integer_binary, decimal_binary)}'
    
    exponent = get_exponent(integer_binary)
    shifted_exp = exponent + 127
    shifted_bin_exp = _dec_to_simple_bin(shifted_exp)
    sign: str = '1' if integer[0] == '-' else '0'
    mantisse = complete_mantisse(exponent, integer_binary, decimal_binary)
    final_IEEE754: str = f'{sign} {shifted_bin_exp} {mantisse}'

    if have_comma:
            cientific_noptation = f'The Full Binary in cientific notation is: {full_binary_base}x2^{exponent}'
    else:
        cientific_noptation = f'The Full Binary in cientific notation is: {full_binary_base}'

    #? ####### Messages to the user ########
    message(
        'Number Part ######',
        f'The Integer part to Binary is: {integer_binary}',
        f'The Decimal part to Binary is: {decimal_binary}',
        f'{cientific_noptation}'
    )

    message(
        '#### Exponent ####',
        f'The exponent in decimal is: {exponent}',
        f'The exponent in binary is: {_dec_to_simple_bin(exponent)}',
        f'The shifted exponent is: {shifted_exp}',
        f'The shifted exponent in binary is: {shifted_bin_exp}'
    )

    message(
        '#### IEEE 754 ######',
        f'The Sign is: {sign}',
        f'The shifted exponent in binary is: {shifted_bin_exp}',
        f'The Mantisse is: {mantisse}',
        f'The Final IEEE 754 String is:',
        f'{final_IEEE754} ##'
    )
