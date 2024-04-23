def StringChallenge(str1, str2):
    varOcg = set(str1)

    # Comprobar si todos los caracteres en str2 están presentes en str1
    if set(str2).issubset(varOcg):
        return 'true'
    else:
        return 'false'