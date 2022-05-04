
from DecToBin_Mod.dec_to_bin import dec_to_IEEE_754 as dec_to_IEEE
from Auxiliar_Mod.auxiliars import get_decimal_input as decimal_input
from Auxiliar_Mod.auxiliars import get_IEEE_754_string as ieee_input
from Auxiliar_Mod.auxiliars import print_menu as menu
from Auxiliar_Mod.auxiliars import print_message as message

#* ######## Basic Configuration ########
app_name: str = 'Converter_IEEE754_Decimal'
version: str = '1.0'
author: str = 'Facu Falcone'
#* ######## input ##########
option: str = menu()
if option == '1':
    dec_number = decimal_input()
    dec_to_IEEE(dec_number)
elif option == '2':
    ieee_number = ieee_input()
    pass
message(
    'Thanks for using this app',
    f'{app_name} | V{version} | by {author}'
)