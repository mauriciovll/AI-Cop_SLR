# Bibliotecas necessárias para conexão à OpenAI
import openai # type: ignore
from dotenv import load_dotenv, find_dotenv # type: ignore
import os   # Biblioteca para manipular o sistema operacional
import pandas as pd    # Biblioteca de manipulação de dados

_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

# Carregar tabela de artigos para verificar possibilidade de inclusão
file_path = '../../data/processed/_7_exclude-verification-file.xlsx'
articles_df = pd.read_excel(file_path)

# Função para analisar título e resumo usando GPT e incluir na lista de artigos do portfolio
def include_to_portfolio(title, abstract):
    prompt = f"""
    Você é um especialista em análise de literatura científica. Sua tarefa é analisar se o seguinte artigo se alinha com os critérios de inclusão para um estudo sobre tecnologias emergentes e dados no setor público. 
    
    Critérios de inclusão:
    1. O artigo deve abordar o tema de tecnologias emergentes e/ou dados, tais como inteligência artificial, aprendizado de máquina, análise de dados, big data, internet das coisas, blockchain, entre outros.
    2. O artigo deve discutir o tema no contexto do setor público, envolvendo tópicos como administração pública, políticas públicas, serviços públicos ou organizações governamentais.
    3. A perspectiva da discussão deve ser "de dentro para fora" do governo, ou seja, o artigo deve analisar casos, práticas, ou implementações de tecnologias emergentes dentro de organizações públicas ou utilizar organizações públicas como objeto de análise.

    Com base nesses critérios, leia atentamente o título e o resumo abaixo e responda apenas com '1' se o artigo atender aos critérios ou '0' se não atender.
    
    Título: {title}
    Resumo: {abstract}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Ou "gpt-4" se estiver disponível para você
        messages=[
            {"role": "system", "content": "Você é um assistente de análise científica."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=50,  # Ajuste conforme necessário
        temperature=0
    )

    # Extrair a resposta
    result = response.choices[0].message['content'].strip()
    return result

# Aplicar a análise em cada artigo
articles_df['Entra?'] = articles_df.apply(lambda row: include_to_portfolio(row['title'], row['abstract']), axis=1)

# Salvar o resultado em um novo arquivo Excel
output_file_path = '../../data/processed/_8_exclude-verified-file.xlsx'
articles_df.to_excel(output_file_path, index=False)