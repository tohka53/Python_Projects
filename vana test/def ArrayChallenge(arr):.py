def ArrayChallenge(arr):
    arr= [5,10,15]
    min_num = min(arr)
    max_num = max(arr)

    varOcg = max_num - min_num + 1

    missing_nums = varOcg - len(arr)

    return missing_nums

