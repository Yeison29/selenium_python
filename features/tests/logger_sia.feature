Feature: Logearse en el sia

  Scenario Outline: Como usuraio de la UFPSO quiero iniciar sesion en el SIA
    Given para iniciar session nesesito ingresar en la pagina https://siaweb.ufpso.edu.co/
    When ingrese los sigueintes datos <codigo>, <documento> y <contrasena>
    And Click en ingresar
    Then se inicio sesion correctamente validando con la palabra Usuario Autenticado

    Examples:
      | codigo | documento  | contrasena         |
      | 191829 | 1005074695 | YDascanioascanio29 |
      | 191829 | 1005074698 | YDascanioascanio29 |
      | 191829 | 1005074695 | YDascanioascanio   |
      | 191846 | 1007561307 | DignayPablo123!    |
      | 191845 | 1007561307 | DignayPablo123!    |