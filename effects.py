from PySide2.QtCore import *
from PySide2 import QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from random import randrange
from threading import Timer
import threading
from login_pyside24 import Ui_MainWindow
from login_pyside24 import *


EXPAND_CARD = 80;
EXPAND_CARD2 = 80;
HIDE_CARDS = 0;


class GeneralEffects(Ui_MainWindow):
            return icon

class SlideEffects(Ui_MainWindow):
    
    def _launch_details_slide(self):
        self.stackedWidget_58.setTransitionDirection(QtCore.Qt.Horizontal)
        self.stackedWidget_58.setTransitionSpeed(250)
        self.stackedWidget_58.setTransitionEasingCurve(QtCore.QEasingCurve.InExpo)
        self.stackedWidget_58.setSlideTransition(True)
    
    def main_menu(self): #TODO MAIN TRANSITION
        self.stacked_configcartao0.setTransitionDirection(QtCore.Qt.Horizontal)
        self.stacked_configcartao0.setTransitionSpeed(250)
        self.stacked_configcartao0.setTransitionEasingCurve(QtCore.QEasingCurve.OutExpo)
        self.stacked_configcartao0.setSlideTransition(True)
        
    def grid_cards(self):
        self.stackedWidget_3.setTransitionDirection(QtCore.Qt.Horizontal)
        self.stackedWidget_3.setTransitionSpeed(250)
        self.stackedWidget_3.setTransitionEasingCurve(QtCore.QEasingCurve.InExpo)
        self.stackedWidget_3.setSlideTransition(True)
    
    def _general_card_content(self):
        self.detalhes_cartao.setTransitionDirection(QtCore.Qt.Horizontal)
        self.detalhes_cartao.setTransitionSpeed(250)
        self.detalhes_cartao.setTransitionEasingCurve(QtCore.QEasingCurve.InExpo)
        self.detalhes_cartao.setSlideTransition(True)

    def _add_banks_credits(self):
        self.stackedWidgetadc_2.setTransitionDirection(QtCore.Qt.Horizontal)
        self.stackedWidgetadc_2.setTransitionSpeed(250)
        self.stackedWidgetadc_2.setTransitionEasingCurve(QtCore.QEasingCurve.InExpo)
        self.stackedWidgetadc_2.setSlideTransition(True)

    def lateral_menu_grid(self, button):
        
        btn = button
        duration = 50 #animation duration
        geometry = 0
        if btn == "account":
            self.stackedWidget_2.setCurrentWidget(self.page_1)       
            geometry = 60
        if btn == "investment":
            self.stackedWidget_2.setCurrentWidget(self.page_4)
            geometry = 180
        if btn == "card":
            self.stackedWidget_2.setCurrentWidget(self.page_3)
            geometry = 120
        if btn == "transfer":
            self.stackedWidget_2.setCurrentWidget(self.page_5)
            geometry = 240
        if btn == "stock":
            self.stackedWidget_2.setCurrentWidget(self.page_6)
            geometry = 300
        if btn == "config" :
            self.stackedWidget_2.setCurrentWidget(self.page_6)
            geometry = 360
        if btn == "dev":
            self.stackedWidget_2.setCurrentWidget(self.page_7)
            geometry = 420


            
        self.stackedWidget_2.setTransitionDirection(QtCore.Qt.Horizontal)
        self.stackedWidget_2.setTransitionSpeed(350)
        self.stackedWidget_2.setTransitionEasingCurve(QtCore.QEasingCurve.OutExpo)
        self.stackedWidget_2.setSlideTransition(True)
        
        self.animA = QPropertyAnimation(self.animcurretnpage, b"geometry")
        self.animA.setDuration(duration)
        self.animA.setStartValue(QRect(self.animcurretnpage.geometry()))
        self.animA.setEndValue(QRect(0, geometry, 4, 60))
        self.animA.start()
        
    
    
    def grid_filter(self, direction, object):
        btn = direction
        duration = 600 #animation duration
        geometry = 0
        
        withs = self.extrat_meses.frameGeometry().width()
        if btn == "Next":
            self.animation = QPropertyAnimation(object, b"maximumWidth")
            self.animation.setDuration(duration)
            self.animation.setStartValue(0)
            self.animation.setEndValue(withs)
            self.animation.setEasingCurve(QEasingCurve.OutExpo)
            self.animation.start()
            
  
        if btn == "Previous":
            self.animation = QPropertyAnimation(object, b"maximumWidth")
            self.animation.setDuration(duration)
            self.animation.setStartValue(0)
            self.animation.setEndValue(withs)
            self.animation.setEasingCurve(QEasingCurve.OutExpo)
            self.animation.start()
        
        
        
    def grid_not_found(self):
        self.stack_extrato_pages.setTransitionDirection(QtCore.Qt.Vertical)
        self.stack_extrato_pages.setTransitionSpeed(200)
        self.stack_extrato_pages.setTransitionEasingCurve(QtCore.QEasingCurve.OutExpo)
        self.stack_extrato_pages.setSlideTransition(True)
        
        
    
    def _hide_group_cards(self):

        duration = 600 #animation duration
        geometry = 0
        object = self.content_cartao
        global HIDE_CARDS
        
        
        if HIDE_CARDS == 1:
            self.animation = QPropertyAnimation(object, b"maximumWidth")
            self.animation.setDuration(duration)
            self.animation.setStartValue(0)
            self.animation.setEndValue(440)
            self.animation.setEasingCurve(QEasingCurve.OutExpo)
            self.animation.start()
            HIDE_CARDS = 0
            icon = QIcon()
            icon.addFile(u":/backgroud/src-page-cartoes/back.png", QSize(), QIcon.Normal, QIcon.Off)
            self.hide_cards_main.setIcon(icon)
            self.hide_cards_det.setIcon(icon)

            
  
        else:
            self.animation = QPropertyAnimation(object, b"maximumWidth")
            self.animation.setDuration(duration)
            self.animation.setStartValue(440)
            self.animation.setEndValue(0)
            self.animation.setEasingCurve(QEasingCurve.OutExpo)
            self.animation.start()
            HIDE_CARDS = 1
            icon14 = QIcon()
            icon14.addFile(u":/backgroud/src-page-cartoes/next.png", QSize(), QIcon.Normal, QIcon.Off)
            self.hide_cards_main.setIcon(icon14)
            self.hide_cards_det.setIcon(icon14)

    def _icon_main(self, id):
    
        if id == 'C6':
            icon = "url(:/menu/c6.jpg)"
            return icon
        if id == 'NUBANK':   
            icon = "url(:/menu/nu-icon.png)"
            return icon
        if id == 'BTG':
            icon = "url(:/menu/btg-icon.png)"
            return icon
        if id == 'SANTANDER':
            icon = "url(:/menu/santander-icon.png)"
            return icon
        if id == 'ITAU':
            icon = "url(:/menu/itau-icon.png)"
            return icon
        if id == 'BRADESCO':
            icon = "url(:/menu/bradesco-icon.png)"
            return icon
        if id == 'CAIXA ECONOMICA':
            icon = "url(:/menu/caixa-icon.png)"
            return icon

    def _icon_main_path(self, id):
    
        if id == 'C6':
            icon = ":/menu/c6.jpg"
            return icon
        if id == 'NUBANK':   
            icon = ":/menu/nu-icon.png"
            return icon
        if id == 'BTG':
            icon = ":/menu/btg-icon.png"
            return icon
        if id == 'SANTANDER':
            icon = ":/menu/santander-icon.png"
            return icon
        if id == 'ITAU':
            icon = ":/menu/itau-icon.png"
            return icon
        if id == 'BRADESCO':
            icon = ":/menu/bradesco-icon.png"
            return icon
        if id == 'CAIXA ECONOMICA':
            icon = ":/menu/caixa-icon.png"
            return icon




class HoverEventFrames(Ui_MainWindow):
    
    def _btns_top_main(self, event):
        default = self.frame_43.frameGeometry().width()
        
        if event == 'enter':
            maximum = 200
            
            self.animation = QPropertyAnimation(self.frame_43, b"minimumWidth")
            self.animation.setDuration(1000)
            self.animation.setStartValue(default)
            self.animation.setEndValue(maximum)
            self.animation.setEasingCurve(QEasingCurve.OutExpo)
            self.animation.start()
            #text
            self.hide_cards_main_2.setText("     Function")
            self.pushButton_24.setText("     Cards")
            self.show_cards_main_2.setText("   Dashboard")
        else:
            maximum = 80
            
            self.animation = QPropertyAnimation(self.frame_43, b"minimumWidth")
            self.animation.setDuration(1000)
            self.animation.setStartValue(default)
            self.animation.setEndValue(maximum)
            self.animation.setEasingCurve(QEasingCurve.OutExpo)
            self.animation.start()

            #text
            self.hide_cards_main_2.setText("")
            self.pushButton_24.setText("")
            self.show_cards_main_2.setText("")
        


class EnableSlide(Ui_MainWindow):

    def _slide(self, stackedwidget_SET):
        self.widget = stackedwidget_SET
        self.widget.setTransitionDirection(QtCore.Qt.Vertical)
        self.widget.setTransitionSpeed(200)
        self.widget.setTransitionEasingCurve(QtCore.QEasingCurve.OutExpo)
        self.widget.setSlideTransition(True)
        return True
