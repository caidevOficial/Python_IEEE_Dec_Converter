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

import tkinter as tk
import customtkinter
import warnings
from tkinter.messagebox import showwarning as warning
from modules import (
    dec_to_IEEE754, get_report_dec_to_IEEE_754, IEEE754_to_dec, validate_input
)

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title(f"IEEE Converter")
        self.minsize(320, 250)

        self.__data = {
            'app_name' : 'Converter IEEE754 Decimal',
            'version' : '2.0',
            'author' : 'Facu Falcone'
        }

        self.__label_title = customtkinter.CTkLabel(
            master=self, text=f"{self.__data['app_name']} | V{self.__data['version']} | By {self.__data['author']}", 
            font=("Arial", 20, "bold"))
        self.__label_title.grid(row=0, column=0, columnspan=5, padx=20, pady=10)

        self.image = tk.PhotoImage(file='./assets/img/UTN_Ieee_Decimal_App_v2.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 5, sticky = 'we')

        self.__txt_ieee_str_in = customtkinter.CTkEntry(master=self, placeholder_text='IEEE 754 Input')
        self.__txt_ieee_str_in.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky = 'we')

        self.__btn_bin_to_dec = customtkinter.CTkButton(master=self, text="➡️ Bin to Dec ➡️", command=self.btn_bin_to_dec_on_click)
        self.__btn_bin_to_dec.grid(row=2, column=2, pady=10, columnspan=1, sticky="nsew")

        self.__txt_dec_str_out = customtkinter.CTkEntry(master=self, placeholder_text='Decimal Output')
        self.__txt_dec_str_out.grid(row=2, column=3, columnspan=2, padx=10, pady=10, sticky = 'we')

        self.__txt_dec_str_in = customtkinter.CTkEntry(master=self, placeholder_text='Decimal Input')
        self.__txt_dec_str_in.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky = 'we')

        self.__btn_dec_to_bin = customtkinter.CTkButton(master=self, text="➡️ Dec to Bin ➡️", command=self.btn_dec_to_bin_on_click)
        self.__btn_dec_to_bin.grid(row=3, column=2, pady=10, columnspan=1, sticky="nsew")

        self.__txt_ieee_str_out = customtkinter.CTkEntry(master=self, placeholder_text='IEEE 754 Output')
        self.__txt_ieee_str_out.grid(row=3, column=3, columnspan=2, padx=10, pady=10, sticky = 'we')

    def btn_bin_to_dec_on_click(self):
        """
        The function converts a binary string representing an IEEE 754 number to its decimal equivalent
        and updates the output field with the result.
        """
        bin_str = self.__txt_ieee_str_in.get()
        if not validate_input(bin_str, 'Bin'):
            warning('Invalid IEEE', 'The IEEE Binary number hasn`t the correct format')
        else:
            dec_output = IEEE754_to_dec(bin_str)
            self.__txt_dec_str_out.delete(0, tk.END)
            self.__txt_dec_str_out.insert(0, dec_output)

    def btn_dec_to_bin_on_click(self):
        """
        The function converts a decimal number to its IEEE 754 representation and updates the output
        text field with the result.
        """
        dec_str = self.__txt_dec_str_in.get()
        if not validate_input(dec_str, 'Dec'):
            warning('Invalid Decimal', 'The Decimal number hasn`t the correct format')
        else:
            ieee_out = dec_to_IEEE754(float(dec_str))
            self.__txt_ieee_str_out.delete(0, tk.END)
            self.__txt_ieee_str_out.insert(0, ieee_out)
            get_report_dec_to_IEEE_754(dec_str)

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()