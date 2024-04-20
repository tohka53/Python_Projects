def ArrayChallenge(arr):
    arr= [5,10,15]
    # __define-ocg__: Encontrar el número mínimo de enteros necesarios para hacer que los contenidos de arr sean consecutivos
    min_num = min(arr)
    max_num = max(arr)

    # Calcular la cantidad de números que deberían estar en el rango desde el mínimo hasta el máximo
    varOcg = max_num - min_num + 1

    # Restar la longitud de arr de este número para encontrar cuántos números faltan para hacer que arr sea consecutivo
    missing_nums = varOcg - len(arr)

    return missing_nums

