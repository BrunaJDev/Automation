📄 Script de Automação para Mesclagem de PDFs

📌 Sobre o Projeto
Este script, desenvolvido em Python, automatiza o processo de mesclagem de arquivos PDF, facilitando a junção de múltiplos documentos em um único arquivo de forma rápida e eficiente.

🚀 Tecnologias Utilizadas
Python 3
Os (para manipulacao do arquivo pdf dentro da pasta)
PyPDF2 (Manipulacao de pdf)

📝 Passo 1: Instalar as Bibliotecas terminal do editor (Usei o Vscode)

  comando para instalar: pip install PyPDF2

📝 Passo 2: Importar as Bibliotecas
    import PyPDF2
    import os #(biblioteca para acessar arquivos dentro da pasta)

📝 Passo 3: Criando um objeto que mescla arquivos

   Aqui criamos um objeto merger usando a classe PdfMerger() da biblioteca PyPDF2 para mesclar arquivos PDF por meio de seu método append().
      merger = PyPDF2.PdfMerger() 
   
   Em seguida, acessamos a pasta "Archive" (pasta nomeada que contém pdf), listamos os arquivos e ordenamos a lista. 
      lista = os.listdir("Archive") #aqui criamos uma var para listar aquivos dentro da pasta direcionada
      lista.sort()
      
📝 Passo 4: Onde a mágica acontece
 Para cada arquivo PDF na lista, verificamos se ele tem a extensão .pdf e, se sim, o adicionamos ao objeto merger. Esse Objeto merger será responsavel por mesclar os pdfs
   #Condicao para mesclar
        for Archive in lista:
          if ".pdf" in Archive:   #Verificar se o arquivo é pdf
          merger.append(f"Archive/{Archive}")  #Adciona a pasta co seus arqqivos no mesclador
          #merger.append("nome da pasta/{nome da pasta}")

📝 Passo 5: Salvar o PDF Mesclado
   merger.write("PDF mesclado.pdf")
