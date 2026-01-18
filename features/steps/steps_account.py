from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError
from selenium.webdriver.common.by import By

@given(u'Je suis sur la page de creation de compte campus france')
def step_impl(context):
    driver = context.driver
    context.js = driver.execute_script  # maintenant ça fonctionne
    driver.get("https://www.campusfrance.org/fr/user/register")

@when(u'je renseigne les champs avec un profil etudiant et je coche la case des conditions')
def step_impl(context):
    p = context.personne
    driver = context.driver
    js = context.js

    # Accepter cookies
    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/button[2]").click()

    # Champs email et mot de passe
    driver.find_element(By.XPATH, "//form/div[2]/div/div[1]/input").send_keys(p.email)
    driver.find_element(By.XPATH, "//form/div[2]/div/div[2]/div[1]/input").send_keys(p.motDePasse)
    driver.find_element(By.XPATH, "//form/div[2]/div/div[2]/div[2]/input").send_keys(p.confirmationMotDePasse)

    # Nom et prénom
    js("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH,
                                                                 "/html/body/div[2]/div[2]/main/div[2]/div/div[2]/form/div[3]/h2"))
    driver.find_element(By.XPATH, "//form/div[3]/div[1]/fieldset/div/div/div[1]/label").click()
    driver.find_element(By.ID, "edit-field-nom-0-value").send_keys(p.nom)
    driver.find_element(By.ID, "edit-field-prenom-0-value").send_keys(p.prenom)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/button[2]").click()
    # Pays de résidence
    driver.find_element(By.XPATH, "//form/div[3]/div[4]/div/div/div[1]").click()
    france = driver.find_element(By.XPATH, "//form/div[3]/div[4]/div/div/div[2]/div/div[164]")
    js("arguments[0].parentElement.scrollTop = arguments[0].offsetTop;", france)
    france.click()

    # Autres informations personnelles
    driver.find_element(By.ID, "edit-field-nationalite-0-target-id").send_keys(p.paysDeNationalite)
    driver.find_element(By.ID, "edit-field-code-postal-0-value").send_keys(p.codePostal)
    driver.find_element(By.ID, "edit-field-ville-0-value").send_keys(p.ville)
    driver.find_element(By.ID, "edit-field-telephone-0-value").send_keys(p.telephone)

    # Domaine et niveau d'études
    js("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH,
                                                                 "//form/div[4]/div[1]/fieldset/div/div/div[3]/label"))
    #driver.find_element(By.XPATH, "//form/div[4]/div[2]/div[1]/div/div/div[1]").click()
    element = driver.find_element(By.XPATH, "//form/div[4]/div[2]/div[1]/div/div/div[1]")
    driver.execute_script("arguments[0].click();", element)

    informatique = driver.find_element(By.XPATH, "//form/div[4]/div[2]/div[1]/div/div/div[2]/div/div[12]")
    js("arguments[0].parentElement.scrollTop = arguments[0].offsetTop;", informatique)
    context.js("arguments[0].click();", informatique)

    #driver.find_element(By.XPATH, "//form/div[4]/div[2]/div[2]/div/div/div[1]").click()
    context.js("arguments[0].click();", driver.find_element(By.XPATH, "//form/div[4]/div[2]/div[2]/div/div/div[1]"))

    master2 = driver.find_element(By.XPATH, "//form/div[4]/div[2]/div[2]/div/div/div[2]/div/div[9]")
    js("arguments[0].parentElement.scrollTop = arguments[0].offsetTop;", master2)
    context.js("arguments[0].click();", master2)
    #master2.click()

    driver.find_element(By.XPATH, "//form/div[4]/div[4]/div/label").click()

@then(u'le texte dans le bouton creer est CREER UN COMPTE')
def step_impl(context):
    driver = context.driver
    js = context.js
    js("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "//*[@id='edit-submit']"))
    text = driver.find_element(By.XPATH, "//form/div[5]/input").get_attribute("value")
    assert text == "Créer un compte"