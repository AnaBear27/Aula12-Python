nome_arquivo = input("Digite o nome do arquivo de texto: ")

with open(nome_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
    
palavras = conteudo.split()
numeros_palavras = len(palavras)

print(f"O arquivo '{nome_arquivo}' possui {numeros_palavras} palavras.")