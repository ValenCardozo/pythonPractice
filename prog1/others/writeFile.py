# Formas de escritura:
# w: sobreescribe
# a: agrega al final del archivo

# 1. write()
# with open('others/names.text', 'w') as names:
#     names.write('Sara\nMiguel\nRoberto\nAna\n')

# 2. writelines()
with open('others/names.text', 'w') as names:
    list = ['Sara\n','Miguel\n','Roberto\n','Ana\n']
    names.writelines(list)