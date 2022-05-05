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
message('#',
    'Thanks for using this app',
    f'{app_name} | V{version} | by {author}'
)