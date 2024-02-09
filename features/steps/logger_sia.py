from behave import given, when, step, then, use_step_matcher
from selenium.webdriver.common.by import By
from time import sleep

use_step_matcher("re")

INPUT_COD = (By.NAME, 'cod')
INPUT_DOC = (By.NAME, 'doc')
INPUT_PASS = (By.NAME, 'pas')
BTN_LOGIN = (By.ID, 'ingresar')
ALERT = (By.CLASS_NAME, 'nota_contenido')


@given('para iniciar session nesesito ingresar en la pagina (.*)')
def step_given_ingresar_pagina(context, url):
    """
    :param url: URL de la página de inicio de sesion
    :type context: behave.runner.Context
    """
    print(f'Ingresando a la pagina: {url}')
    context.driver.get(url)
    # raise NotImplementedError(
    #     f'STEP: Given para iniciar session nesesito ingresar en la pagina: {url}')


@when("ingrese los sigueintes datos (.*), (.*) y (.*)")
def step_ingresar_datos(context, codigo, documento, contrasena):
    """
    :param contrasena: Contraseña del usuario
    :param documento: N° docuemnto del usuario
    :param codigo: N° codigo del usuario
    :type context: behave.runner.Context
    """
    print(f"Ingresando datos: {codigo}, {documento}, {contrasena}")

    input_code = context.driver.find_element(*INPUT_COD)
    input_doc = context.driver.find_element(*INPUT_DOC)
    input_pas = context.driver.find_element(*INPUT_PASS)

    input_code.clear()
    input_doc.clear()
    input_pas.clear()

    input_code.send_keys(codigo)
    input_doc.send_keys(documento)
    input_pas.send_keys(contrasena)
    sleep(4)


@step("Click en ingresar")
def step_btn_ingresar(context):
    """
    :type context: behave.runner.Context
    """
    print(f'Ingresando')
    context.driver.find_element(*BTN_LOGIN).click()
    sleep(1)


@then("se inicio sesion correctamente validando con la palabra (.*)")
def step_(context, validator):
    """
    :type context: behave.runner.Context
    """
    sleep(5)
    try:
        text_element_valid = context.driver.find_element(*ALERT).text
        if text_element_valid.lower() == validator.lower():
            print("Se inicio sesion correctamente")
        elif (text_element_valid.lower() == "Error de Autenticación".lower() or
              text_element_valid.lower() == "Datos Erróneos".lower()):
            print("Credenciales incorrectos")
        else:
            print("Supero el numero maximo de intentos")
    except Exception as e:
        print("No se encontro el alert", e)
