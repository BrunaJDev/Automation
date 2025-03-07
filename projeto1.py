#Projeto de script para automatizar a mesclagem de PDF's
#Intalar a biblioteca no terminal

#Importando a biblioteca que faz isso
import PyPDF2
import os #(biblioteca para acessar arquivos dentro da pasta)

merger = PyPDF2.PdfMerger() #criando um objeto que mescla arquivos

#Acessando a pasta que contém o pdf e colocando dentro de uma var
lista = os.listdir("Archive")
#ordenando a lista:
lista.sort()
print(lista)

#Condicao para mesclar
for Archive in lista:
    if ".pdf" in Archive:   #Verificar se o arquivo é pdf
      merger.append(f"Archive/{Archive}")  #Adciona a pasta no mesclador
      #merger.append("nome da pasta/{nome da pasta}")

#Salvando o pdf mesclado
#Salva em pdf e nomeia o arquivo
merger.write("PDF mesclado.pdf")