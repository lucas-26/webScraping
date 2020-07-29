import sys 
import os
import re
import http
import pyautogui
from htmldom import htmldom
from urllib.request import urlopen
from bs4 import BeautifulSoup 
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pyautogui
import inspect 
import time

now = datetime.now()
opt = Options() 

def acessar_unicid(obj):
    if obj is None: 
        browser.quit()


browser = webdriver.Chrome(options=opt)
browser.get('https://meuportal.cruzeirodosul.edu.br/alunos/novo_login.jsp')

found = browser.find_element_by_id('rgm_alun')
acessar_unicid(found)
found.send_keys('')


found = browser.find_element_by_id('senha')
acessar_unicid(found)
found.send_keys('')

found = browser.find_element_by_css_selector('input[value="Entrar"]').click()

time.sleep(3)

link = browser.find_element_by_link_text('Área do Aluno').click()

el = browser.find_elements_by_class_name('dhx_acc_item_label')
found = None 

for e in el:
        if e.text == 'Financeiro':
                found = e
                break
found.click()

browser.switch_to.frame(3)


botaoBoleto = browser.find_element_by_partial_link_text('Boleto Bancário')
botaoBoleto.click()

browser.switch_to.default_content()

browser.switch_to.frame(0)

form_lupa = browser.find_element_by_id('formPrincipal')

div_formulario_principal = browser.find_element_by_xpath("//*[@id='formPrincipal:j_idt16']/div")

div_formulario_boleto = browser.find_element_by_xpath("//*[@id='formPrincipal:j_idt16']/div")

try:

                botao_lupa = browser.find_element_by_xpath("//*[@id='formPrincipal:j_idt16:0:j_idt25']/span[1]")

                botao_lupa.click()

                time.sleep(3)

                pyautogui.moveTo(460,460, duration=2)

                pyautogui.rightClick(460,460)

                pyautogui.moveTo(495,495,duration=2)

                pyautogui.click(495, 495)

                pyautogui.moveTo(200, 200, duration=2)

                pyautogui.click(200,200)

                pyautogui.moveTo(520,450, duration=2)

                pyautogui.click(480,390);pyautogui.typewrite("boltetoo", now)

                pyautogui.click(520, 450)
except:
                botao_lupa = browser.find_element_by_xpath("//*[@id='formPrincipal:j_idt16:0:j_idt26']/span[1]")
                
                botao_lupa.click()

                pyautogui.moveTo(580,510, duration=2)

                pyautogui.click(580,510)

        
