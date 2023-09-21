import pandas as pd

def cadastro(nome,preco,categoria,marca,codigo):
    
    try:
        df = pd.read_excel('cadastros.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Nome','Preço','Categoria','Marca'])
    
    dados_produto = {
        'Código': codigo,
        'Nome': nome,
        'Preço': preco,
        'Categoria': categoria,
        'Marca': marca
    }
    
    df = df._append(dados_produto, ignore_index=True)
    
    df.to_excel("cadastros.xlsx", index=False)