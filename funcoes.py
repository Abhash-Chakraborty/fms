from PySide2.QtCore import *
from PySide2 import QtWidgets
from PySide2.QtGui import *
import pyautogui
import os.path
from threading import Timer
import threading
from time import sleep
import effects
from datetime import date


class GeneralFunctions():
    def installment(self):
        
        if self.table_january_4.item(0, 4).text() == 'INSTALLMENT':
            pyautogui.alert('WOULD YOU LIKE TO PAY IN INSTALLMENTS?')

    
    def date_and_time(self):
        
        current_date = date.today()
        date_in_text = current_date.strftime('%m/%Y')
