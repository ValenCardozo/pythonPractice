# Abrir un archivo .txt

# 1. Apertura de contexto read()
# with open('others/file.txt') as file:
    # puntero al inicio del file
    # print(file.tell())
    # Todo el contenido del file
    # allFile = file.read()
    # print(allFile)
    # puntero al final del file
    # print(file.tell())

    # mover el puntero y leer cierta cantidad de caracteres
    # file.seek(5)
    # word = file.read(11)
    # print(word)

# 2. readline()
# with open('others/file.txt') as file:
#     print(file.readline())

# 3. readlines()
# with open('others/file.txt') as file:
#     print(file.readlines())

# 4. recorrer por for
with open('others/file.txt') as file:
    for line in file:
        print(line, end='')