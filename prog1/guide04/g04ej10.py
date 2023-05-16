# Determinar cuál es la vocal que aparece con mayor frecuencia

text = 'Quiero comer manzanas, solamente manzanas.'
vocals = ['a', 'e', 'i', 'o', 'u']
moreAppears = 'a'
maxCount = 0

for vocal in vocals:
    countVocal = 0
    for caracter in text:
        if caracter == vocal:
            countVocal += 1
    
    if countVocal > maxCount:
        moreAppears = vocal
        maxCount = countVocal

print(moreAppears)