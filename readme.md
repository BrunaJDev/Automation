📄 Script de Automação para Mesclagem de PDFs <br>

📌 Sobre o Projeto <br>
Este script, desenvolvido em Python, automatiza o processo de mesclagem de arquivos PDF, facilitando a junção de múltiplos documentos em um único arquivo de forma rápida e eficiente.

🚀 Tecnologias Utilizadas <br>
Python 3 <br>
Os (para manipulacao do arquivo pdf dentro da pasta) <br>
PyPDF2 (Manipulacao de pdf) <br> 

📝 Passo 1: Instalar as Bibliotecas terminal do editor (Usei o Vscode) <br>

  comando para instalar: pip install PyPDF2 <br>

📝 Passo 2: Importar as Bibliotecas<br>
    import PyPDF2 <br>
    import os #(biblioteca para acessar arquivos dentro da pasta)<br>

📝 Passo 3: Criando um objeto que mescla arquivos<br>

   Aqui criamos um objeto merger usando a classe PdfMerger() da biblioteca PyPDF2 para mesclar arquivos PDF por meio de seu método append().<br>
      merger = PyPDF2.PdfMerger()<br>
   
   Em seguida, acessamos a pasta "Archive" (pasta nomeada que contém pdf), listamos os arquivos e ordenamos a lista. <br> <br>
      lista = os.listdir("Archive") #aqui criamos uma var para listar aquivos dentro da pasta direcionada <br>
      lista.sort()<br>
      
📝 Passo 4: Onde a mágica acontece<br>
 Para cada arquivo PDF na lista, verificamos se ele tem a extensão .pdf e, se sim, o adicionamos ao objeto merger. Esse Objeto merger será responsavel por mesclar os pdfs <br>
   #Condicao para mesclar <br> <br>
        for Archive in lista: <br>
          if ".pdf" in Archive:   #Verificar se o arquivo é pdf <br>
          merger.append(f"Archive/{Archive}")  #Adciona a pasta co seus arqqivos no mesclador <br>
          #merger.append("nome da pasta/{nome da pasta}")<br>

📝 Passo 5: Salvar o PDF Mesclado <br>
   merger.write("PDF mesclado.pdf") # Salva o PDF mesclado com o nome especificado <br>
