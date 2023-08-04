# Project File Organizer #

import os
import shutil

# Muda de diretorio, para o Downloads #
os.chdir('/home/nuvemff/Downloads')
path = ('/home/nuvemff/Downloads')

list_of_files = os.listdir(path)

# Para cada "file" na lista de arquivos em Downloads #
# separa o nome do arquivo da extensão #
# e remove o ponto anterior a extensão #
for file in list_of_files:
    name, ext = os.path.splitext(file)
    ext = ext[1:]

# Verifica se já uma pasta criada para cada extensão #
# Caso já exita move os aruivos para sua determinada pasta #
    if os.path.exists(path + '/' + ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
        print('Arquivos movidos com sucesso!')

# Caso ainda não exista uma pasta para uma extensão #
# cria essa pasta e move o arquivo para dentro dela #
    else: 
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
        print('Nova pasta criada e arquivos movidos com sucesso')
