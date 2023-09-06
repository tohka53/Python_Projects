programing_dictonary = {
"Bug":"Error comun de codigo",
"Loop":"El codigo se quedo enciclado"

}

print(programing_dictonary["Bug"])

programing_dictonary["Bug"] = "Error de compilacion"

for key in programing_dictonary:
    print(key)
    print(programing_dictonary[key])