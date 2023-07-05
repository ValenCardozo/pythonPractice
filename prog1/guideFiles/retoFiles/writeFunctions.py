def insertContent(path: str, index: int, content: str):
    count = 0
    newText = ''
    with open(path) as fileContent:
        text = fileContent.read()

    for caracter in text:
        if count == index:
            newText += content
        newText += caracter
        count += 1

    with open(path, 'w') as file:
        file.write(newText)
    
    return

def insertLine(path: str, line: int, content: str):
    count = 1
    newFile = []
    with open(path) as fileContent:
        file = fileContent.readlines()
    
    for fileLine in file:
        if count == line:
            newFile.append(content + '\n')
        newFile.append(fileLine)
        count += 1

    with open(path, 'w') as file:
        file.writelines(newFile)
    return

path = 'write.txt'
insertContent(path, 6, 'chau')
insertLine(path, 2, 'fila nueva')