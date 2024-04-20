def StringChallenge(str1, str2):
    # __define-ocg__: Comprobar si una porción de los caracteres de str1 puede ser reorganizada para coincidir con str2
    varOcg = set(str1)

    # Comprobar si todos los caracteres en str2 están presentes en str1
    if set(str2).issubset(varOcg):
        return 'true'
    else:
        return 'false'