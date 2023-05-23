import requests 
import os 
from zipfile import ZipFile 


def baixar_arquivos(urls, diretorio_destino):
    for url in urls: 
        nome_arquivo = os.path.basename(url)
        caminho_arquivo = os.path.join(diretorio_destino, nome_arquivo)  
        resposta = requests.get(url)
        with open(caminho_arquivo, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        

urls = [
    "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546_571_577.pdf",
    "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546_571_577.xlsx",
    "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN540_RN541_RN542_RN544_546_550_553_571v2_575_576_577.pdf",
    "https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_III_DC_2021_RN_465.2021.v2.pdf",
    "https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf"
]
diretorio_destino = input("Digite o diretório que deseja salvar os arquivos e posteriormente compacta-los: \n")
while not os.path.exists(diretorio_destino): 
    opcao = input("O diretório não existe, o que deseja fazer?\n1 - Criar este diretório.\n2 - Digitar novamente o diretório. ")
    if int(opcao)==1:
        os.makedirs(diretorio_destino)
    else:
        diretorio_destino = input("Digite o diretório que deseja salvar os arquivos e posteriormente compacta-los: \n")
       

def compactar_arquivos(diretorio_origem, nome_arquivo):      
    lista_arquivos = os.listdir(diretorio_origem)
    nome_completo_arquivo = os.path.join(diretorio_origem, nome_arquivo)
    with ZipFile(nome_completo_arquivo, 'w') as zip: 
        for arquivo in lista_arquivos:
            caminho_arquivo = os.path.join(diretorio_origem, arquivo)
            zip.write(caminho_arquivo, arquivo)


diretorio_origem = diretorio_destino #Definido o diretorio de gravação do arquivo em zip como o mesmo diretorio onde irá ser feito o download dos arquivos.
nome_arquivo = input("Qual o nome você deseja atribuir ao arquivo compactado?\n ") + ".zip"

baixar_arquivos(urls, diretorio_destino)
compactar_arquivos(diretorio_origem, nome_arquivo)


