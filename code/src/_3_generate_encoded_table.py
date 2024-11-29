"""
Plano de Implementação: Gerar tabela excel a partir de arquivos json em uma pasta do projeto

1. Verificação de Arquivos json na Pasta: O script buscará na pasta de destino por arquivos .json.

2. Consolidação dos arquivos json no excel: Para cada arquivo json, o script lerá os arquivos e em seguida irá consolidar esses arquivos em um dataframe pandas.

3. Geração de Tabela Excel: O script criará uma tabela em formato .xlsx e incluirá os arquivos json processados na tabela.

4. Salvar Tabela: O script salvará a tabela como um arquivo de nome  "encoded-articles.xlsx" na mesma pasta no projeto.
"""
import os
import pandas as pd
import json

# Caminho para a pasta que contém os arquivos JSON
pasta_json = 'C:/Users/mauri/OneDrive/Repositorios/ETech-Gov-Review/data/processed/encoded-articles'  # Substitua pelo caminho correto

# Lista para armazenar os dados dos arquivos JSON
lista_dados = []

# Obter a lista de todos os arquivos JSON na pasta
arquivos_json = [f for f in os.listdir(pasta_json) if f.endswith('.json')]

# Iterar sobre os arquivos JSON
for nome_arquivo in arquivos_json:
    caminho_arquivo = os.path.join(pasta_json, nome_arquivo)
    # Ler o conteúdo do arquivo JSON
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        dados_json = json.load(f)
        
        # Adicionar o nome do arquivo como uma coluna extra no DataFrame
        dados_json['Nome do Arquivo'] = nome_arquivo
        
        # Adicionar os dados à lista
        lista_dados.append(dados_json)

# Criar um DataFrame com os dados consolidados
df_final = pd.DataFrame(lista_dados)

# Salvar o DataFrame consolidado em um arquivo Excel
df_final.to_excel('C:/Users/mauri/OneDrive/Repositorios/ETech-Gov-Review/data/processed/_9_encoded-articles.xlsx', index=False)

print("Tabela gerada com sucesso como 'encoded-articles.xlsx'.")