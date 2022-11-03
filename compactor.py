import zipfile as zf
import os


class Compactor:
    def __init__(self, name):
        self.name = f'{name}.zip'

    def compress(self, path_content, pwd=None):
        zip_object = zf.ZipFile(self.name, 'w', zf.ZIP_DEFLATED)
        print('Ziping..')

        if type(path_content) is str:
            path_content = [path_content]

        for file in list(path_content):
            if os.path.isfile(file):  # Verifica se é arquivo (ficheiro)
                zip_object.write(file)  # Adiciona ao destino (um '.zip')
            else:  # Se for diretório
                for root, dirs, files in os.walk(file):  # Raiz do diretório indicado
                    for f in files:  # Indica o arquivo (ficheiro) a ser adiciona
                        # Adiciona o arquivo incluindo a sua 'raiz' (Caminho até ele)
                        zip_object.write(os.path.join(root, f))
                        print(f'{os.path.join(root, f)}')

        if pwd:
            pass

        zip_object.close()

