arquivo_origem = input("Digite o nome do arquivo de origem: ")
arquivo_destino = input("Digite o nome do arquivo do destino: ")

with open(arquivo_origem, 'r') as origem, open(arquivo_destino, 'w') as destino:
    conteudo = origem.read()
    
    destino.write(conteudo)
    
print(f"Conteúdo do arquivo '{arquivo_origem}' copiado para '{arquivo_destino}' com sucesso.")