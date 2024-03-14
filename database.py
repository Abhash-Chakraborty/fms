import sqlite3
from PySide2.QtCore import *
import pyautogui
import os.path

class SaveData:
    # TODO: CREATE DATABASE
    def test_db(self):
        while True:
            a = (os.path.dirname(os.path.realpath(__file__)))
            if(os.path.exists(''+a+'/bando_de_valores.db')):
                pyautogui.alert('Database already created in the root folder, so it will not be possible to create a new file. Please access the program settings to delete the existing DB.')
                break
            else:
                pyautogui.alert('Database not found. Creating in the root directory. Please wait.')
                database = sqlite3.connect(''+a+'/bando_de_valores.db')
                cursor = database.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS card_active (id INTEGER, nome_cartao text, titular text, limite REAL, final INTEGER, vencimento text, fechamento text)")
                
                # BANK ACCOUNTS TABLE
                cursor.execute("CREATE TABLE IF NOT EXISTS bank_accounts(id int, saldo_inicial text, nome_banco text, agencia int, num_conta int, titular text, cartao_credito_id text)")
                
                # BALANCE PAYMENTS TABLE
                cursor.execute("CREATE TABLE IF NOT EXISTS balance_payments(id_lancamento int, id_bank int, tipo_e_s text, valor , ref_vencimento text, data_pagamento text, saldo_atual text, id_discount int)")
                
                # ACCOUNT CONFIGURATIONS
                cursor.execute("CREATE TABLE IF NOT EXISTS config_accounts(conta_padrao_bank int)")
                
                # NEW ENTRY
                cursor.execute("CREATE TABLE IF NOT EXISTS new_entry (id_lancamento int, id_bank int, data_lancamento text, category text, payment text, valor int, type text, description text)")
                
                # DUE DATE ENTRY
                cursor.execute("CREATE TABLE IF NOT EXISTS status_entry (id_lancamento int, id_bank int, vencimento text, status_paid text)")
                
                # RECURRING ENTRY
                cursor.execute("CREATE TABLE IF NOT EXISTS config_entry(id_lancamento int, id_bank int, recurring text, recurring_m_d_s_y text, recurring_day text, attachment text)")
                
                # SETS PRIORITY
                cursor.execute("CREATE TABLE IF NOT EXISTS priority_value(id_lancamento int, id_bank int, priority text)")
                
                # PDF PATCHES
                cursor.execute("CREATE TABLE IF NOT EXISTS pdf_patches(id_lancamento int, id_bank int, patch text, date_insert text, date_update text, ref_month text)")
                
                # APPLICATION SETTINGS:
                cursor.execute("CREATE TABLE IF NOT EXISTS app_settings (id int, theme text, hide_show_zeros_in_invoices text, shadow_ui text)")
                
                database.close()
                pyautogui.alert('Database Created in the root directory.')
                
                break
