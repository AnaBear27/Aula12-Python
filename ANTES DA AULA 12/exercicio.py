#importe o módulo pandas como pd


# Dados para consultar
dados = {
    'Produto': [
        'Camiseta', 'Tênis', 'Boné', 'Calça', 'Jaqueta', 'Camiseta', 'Tênis', 'Boné', 'Camiseta',
        'Calça', 'Tênis', 'Camiseta', 'Boné', 'Jaqueta', 'Calça', 'Tênis', 'Camiseta', 'Boné', 'Tênis', 'Jaqueta'
    ],
    'Vendedor': [
        'Ana', 'João', 'Ana', 'Pedro', 'Lucas', 'Ana', 'João', 'Maria', 'Pedro',
        'Maria', 'Lucas', 'João', 'Ana', 'Pedro', 'Lucas', 'Ana', 'Maria', 'João', 'Lucas', 'Pedro'
    ],
    'Valor': [
        50, 200, 30, 120, 250, 60, 180, 35, 55,
        130, 190, 65, 32, 270, 110, 195, 58, 40, 185, 260
    ],
    'Quantidade': [
        2, 1, 4, 2, 1, 3, 1, 5, 2,
        3, 1, 2, 6, 1, 2, 1, 4, 3, 2, 1
    ]
}

#Consulte a documentação do pandas


#Exiba o dataFrame

# Qual foi o total de vendas (Valor x Quantidade) por vendedor?

# Qual produto teve a maior quantidade total vendida?

# Filtre apenas as vendas com Valor acima de R$ 100.

# Adicione uma coluna chamada 'Total' que é o resultado de Valor * Quantidade.

# Ordene o DataFrame pelo total de vendas em ordem decrescente.
