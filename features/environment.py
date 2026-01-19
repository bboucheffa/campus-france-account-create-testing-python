# environment.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from manage_data.read_data import read_data_from_json

def before_all(context):
    #Je pense faut ajouter les options pour le webdriver (mode headless, no sandbox ...etc)

    # Installer et configurer ChromeDriver
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)  # ← AJOUTE ÇA SEULEMENT


    # Charger les données JSON
    context.personnes = read_data_from_json()

def before_scenario(context, scenario):
    if context.personnes:
        context.personne = context.personnes[0]
    else:
        context.personne = None

def after_all(context):
    context.driver.quit()