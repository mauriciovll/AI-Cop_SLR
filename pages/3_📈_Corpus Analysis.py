import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud # type: ignore
import networkx as nx
from itertools import combinations
from collections import Counter
import community as community_louvain # type: ignore

st.header("📈 Corpus Analysis", divider=True)
# Sumário na Sidebar
section = st.sidebar.radio("**Go to**:", 
                           ["Journals Impact Factor",
                            "Journals Citations",
                            "Publication Profile",
                            "Keywords Analysis"])

# Verificar se o portfolio está presente na session_state
if "Portfolio" not in st.session_state and "JIF" not in st.session_state and "Portfolio-citations" not in st.session_state:
    st.error("⚠️ O portfólio não foi carregado. Por favor, volte para a Homepage para carregar os dados.")

else:
    st.markdown("✔️ Portfolio carregado com sucesso!")
    portfolio = st.session_state["Portfolio"]
    tabela_jif = st.session_state["JIF"]
    portfolio_citations = st.session_state["Portfolio-citations"]

    st.markdown(
        "🎯This section presents the general characteristics of the studies in terms of analysis of journals, authors and keywords, and (ii) content analysis – in which we sought to analyze the articles from a methodological perspective and from the context in which the studies were carried out."
        )
    st.divider()

    # Convertendo os nomes dos periódicos para maiúscula para garantir a correspondência
    portfolio['journal'] = portfolio['journal'].astype(str).str.upper()
    tabela_jif['Journal name'] = tabela_jif['Journal name'].astype(str).str.upper()
    # Filtrar os períodicos do portfolio que estão na tabela JIF
    tabela_jif_port = tabela_jif[tabela_jif['Journal name'].isin(portfolio['journal'].unique())]
    #impact_factors = tabela_jif_port['2023 JIF']

    if section == "Journals Impact Factor":
        st.markdown("### Impact factor analysis")
        if tabela_jif_port.empty:
            st.error("Nenhum periódico do portfolio corresponde aos periódicos na tabela JIF.")
        else:
            # Extraindo os fatores de impacto (JIF) desses periódicos
            impact_factors = tabela_jif_port['2023 JIF'].dropna()  # Remover valores nulos
            if not impact_factors.empty:
                # Configurando layout de duas colunas
                col1, col2 = st.columns(2)
                #Criando histograma na coluna 1
                with col1:
                    #st.markdown("### Histogram of impact factors")
                    # Cria histograma
                    plt.figure(figsize=(10,6))
                    sns.histplot(impact_factors, bins=10, kde=True) # Histograma com kernel density estimate (kde)
                    plt.title('Distribution of impact factors')
                    plt.xlabel('Impact Factor (JIF - 2023)')
                    plt.ylabel('Frequency')

                    # Exibir o gráfico na coluna
                    st.pyplot(plt)
                # Criando boxplot na coluna 2
                with col2:
                    #st.markdown("### Boxplot of Impact Factors")

                    # Criando o boxplot com seaborn
                    plt.figure(figsize=(10, 6))
                    sns.boxplot(impact_factors, orient='v')  # Boxplot vertical
                    plt.title('Quartile Distribution of the Impact Factor (JIF - 2023)')
                    plt.xlabel('Impact Factor (JIF - 2023)')

                    # Exibir o gráfico na coluna 2
                    st.pyplot(plt)
                    
    elif section == "Journals Citations":
        if portfolio_citations.empty:
            st.error("Nenhum artigo foi encontrado no corpus da literatura selecionada (Portfolio).")
        else:
            st.markdown("### Journals distribution by citations and impact")
            # Ordenar os periódicos pelo número de citações
            top_journals = tabela_jif_port.sort_values('Total Citations', ascending=False)  #.nlargest(50, 'Total Citations')  # Apliquei o nlargest no DataFrame completo
            top_journals['short name'] = top_journals['Journal name'].apply(lambda x: x[:30] + '...' if len(x) > 30 else x)
            # Criando o scatterplot
            plt.figure(figsize=(20,6))
            sns.scatterplot(
                x='short name', 
                y='Total Citations', 
                size='2023 JIF', 
                data=top_journals, 
                sizes=(100, 1200),  # Controla o tamanho das bolhas
                hue='2023 JIF',    # Colorir as bolhas com base no JIF
                palette='coolwarm', # Paleta de cores
                legend=False
            )
            # Ajustar o gráfico para que os nomes dos journals no eixo X fiquem legíveis
            plt.xticks(rotation=90)  # Rotacionar os nomes dos journals
            # plt.title('Fator de Impacto por Journal e Número de Citações')
            plt.xlabel('Journal')
            plt.ylabel('Citations')

            # Exibir o gráfico com Streamlit
            st.pyplot(plt)
                        
            st.divider()
            st.markdown("### Average impact and citations of journals")
            # Calculando os quartis e o IQR para JIF
            Q4_jif = tabela_jif_port['2023 JIF'].quantile(0.25)  # Q4 é o quartil mais baixo
            Q3_jif = tabela_jif_port['2023 JIF'].quantile(0.50)  # Q3 é quartil intermediário (mediana)
            Q2_jif = tabela_jif_port['2023 JIF'].quantile(0.75)  # Q2 é o segundo quartil
            Q1_jif = tabela_jif_port['2023 JIF'].max()  # Q1 é o valor mais alto

            # Calculando os limites para identificar outliers em JIF
            IQR_jif = Q2_jif - Q4_jif  # Intervalo interquartil
            lower_bound_jif = Q4_jif - 1.5 * IQR_jif
            upper_bound_jif = Q2_jif + 1.5 * IQR_jif

            # Filtrando os periódicos para remover os outliers de JIF
            filtered_jif = tabela_jif_port[(tabela_jif_port['2023 JIF'] >= lower_bound_jif) & (tabela_jif_port['2023 JIF'] <= upper_bound_jif)]

            # Repetir o processo para Citações
            Q4_citations = tabela_jif_port['Total Citations'].quantile(0.25)  # Quartil mais baixo
            Q3_citations = tabela_jif_port['Total Citations'].quantile(0.50)  # Mediana
            Q2_citations = tabela_jif_port['Total Citations'].quantile(0.75)  # Quartil mais alto
            Q1_citations = tabela_jif_port['Total Citations'].max()  # Valor mais alto

            # Calculando os limites para identificar outliers em citações
            IQR_citations = Q2_citations - Q4_citations  # Intervalo interquartil
            lower_bound_citations = Q4_citations - 1.5 * IQR_citations
            upper_bound_citations = Q2_citations + 1.5 * IQR_citations

            # Filtrando os periódicos para remover os outliers de citações
            filtered_citations = tabela_jif_port[(tabela_jif_port['Total Citations'] >= lower_bound_citations) & (tabela_jif_port['Total Citations'] <= upper_bound_citations)]

            # Calculando as métricas excluindo os outliers
            mean_jif_no_outliers = filtered_jif['2023 JIF'].mean()  # Média do fator de impacto sem outliers
            mean_citations_no_outliers = filtered_citations['Total Citations'].mean()  # Média de citações sem outliers

            # Criando layout com colunas para as métricas
            col1, col2 = st.columns(2)
            # Média do fator de impacto
            with col1:
                st.metric(label="Average Impact Factor (JIF) without Outliers", value=f"{mean_jif_no_outliers:.2f}")
            # Média de citações
            with col2:
                st.metric(label="Average Citations without Outliers", value=f"{mean_citations_no_outliers:.2f}")
    
    elif section == "Publication Profile":
        st.markdown("### Evolution of publishing over time")
        # Agrupar os artigos por ano e contar as publicações por ano
        articles_x_years = portfolio.drop_duplicates(subset='title').groupby('year').size().reset_index(name='count')
        # Garantir que a coluna 'year' seja numérica e que não haja valores nulos
        articles_x_years['year'] = pd.to_numeric(articles_x_years['year'], errors='coerce')
        articles_x_years = articles_x_years.dropna()  # Remover linhas com valores nulos
        if articles_x_years.empty:
            st.error("Não há dados válidos para exibir o gráfico de publicações por ano.")
        else:
            # Criar o gráfico com seaborn
            plt.figure(figsize=(20, 6))
            sns.barplot(x='year', y='count', data=articles_x_years, palette='Blues_d')
            # Adicionar rótulos (número de publicações) em cada barra
            plt.title('Publication Evolution by Year')
            plt.xlabel('Year')
            plt.ylabel('Number of Publications')
            # Exibir o gráfico com Streamlit
            st.pyplot(plt)

        st.markdown("### Articles published by journal (> 2)")
        # Remover duplicatas com base no título do artigo antes de contar as publicações
        portfolio_unique_articles = portfolio.drop_duplicates(subset='title')
        # Agrupar por periódico e contar o número de publicações por periódico, considerando apenas artigos únicos
        publications_per_journal = portfolio_unique_articles.groupby('journal').size().reset_index(name='count')
        # Ordenar os periódicos por número de publicações
        publications_per_journal = publications_per_journal.sort_values(by='count', ascending=False)
        if publications_per_journal.empty:
            st.error("Não há dados válidos para exibir o gráfico de publicações por periódico.")
        else:
            # Filtrar periódicos com mais de um artigo publicado
            top_publications = publications_per_journal[publications_per_journal['count'] > 2]
            # Criar o gráfico de barras horizontal
            plt.figure(figsize=(20, 6))  # Ajustar o tamanho da figura
            sns.barplot(x='count', y='journal', data=top_publications, palette='Blues_d')
            # Adicionar rótulos (número de publicações) em cada barra
            for index, value in enumerate(top_publications['count']):
                plt.text(value, index, f'{value}', va='center')  # Adiciona o valor de cada barra
            # Adicionar títulos e rótulos
            plt.title('Publications by Journal (> 2)', fontsize=16)
            plt.xlabel('Number of Publications', fontsize=12)
            plt.ylabel('Journal')
            # Exibir o gráfico no Streamlit
            st.pyplot(plt)

        st.markdown('### Article citations by database')
        if portfolio_citations.empty:
            st.error("Não há dados válidos para exibir o gráfico citações por artigo.")
        else:
            # Criar o gráfico de barras horizontal
            portfolio_citations = portfolio_citations.reset_index() # Resetar o índice para não dar erro ao manipular a coluna 'title'
            plt.figure(figsize=(10, 8))  # Ajustar o tamanho da figura
            portfolio_citations_top25 = portfolio_citations.nlargest(25, 'WOS')
            #Truncar os nomes dos artigos
            portfolio_citations_top25['short name'] = portfolio_citations_top25['title'].apply(lambda x: x[:50] + '...' if len(x) > 50 else x)
            # Ordenar do menor para o maior no eixo Y para o gráfico de barras horizontais (para mostrar as maiores no topo)
            portfolio_citations_top25 = portfolio_citations_top25.sort_values(by='WOS', ascending=True)
            # Configurar o gráfico empilhado
            plt.figure(figsize=(20, 10))
            # Configurando as barras empilhadas
            plt.barh(portfolio_citations_top25['short name'],
                     portfolio_citations_top25['WOS'],
                     color='skyblue',
                     label='WOS',)
            plt.barh(portfolio_citations_top25['short name'],
                     portfolio_citations_top25['Scopus'], 
                     left=portfolio_citations_top25['WOS'],
                     color='lightgreen',
                     label='Scopus')
            plt.barh(portfolio_citations_top25['short name'],
                     portfolio_citations_top25['Scholar Google'], 
                     left=portfolio_citations_top25['WOS'] + portfolio_citations_top25['Scopus'],
                     color='lightcoral',
                     label='Scholar Google')
            # Adicionar rótulos dentro das barras para cada grupo (WOS, Scopus e Scholar Google)
            for i, (wos, scopus, scholar) in enumerate(zip(portfolio_citations_top25['WOS'], 
                                                           portfolio_citations_top25['Scopus'], 
                                                           portfolio_citations_top25['Scholar Google'])):
                plt.text(wos / 2, i, str(int(wos)), va='center', ha='center', color='black')  # Rótulo para WOS no centro
                plt.text(wos + scopus / 2, i, str(int(scopus)), va='center', ha='center', color='black')  # Rótulo para Scopus no centro da barra
                plt.text(wos + scopus + scholar / 2, i, str(int(scholar)), va='center', ha='center', color='black')  # Rótulo para Scholar  Google no centro
            # Adicionar título e rótulos
            plt.title('Citations per Article (Top 25 WOS)', fontsize=16)
            plt.xlabel('Number of Citations')
            plt.ylabel('Article')
            # Ajustar o tamanho da fonte dos rótulos do eixo Y
            plt.yticks(fontsize=12)
            # Adicionar legenda
            plt.legend(loc='right')
            # Exibir o gráfico
            st.pyplot(plt)
    
    elif section == "Keywords Analysis":
        st.markdown('### Word Cloud (Top 100)')
        # Combine todas as palavras-chave em uma única string
        all_keywords = ' '.join(portfolio['keywords'].dropna().astype(str))
        # Gerar a nuvem de palavras
        wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=100).generate(all_keywords)
        # Exibir a nuvem de palavras usando Matplotlib
        plt.figure(figsize=(20, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")  # Remover os eixos para deixar o gráfico mais limpo
        st.pyplot(plt)
                
        st.markdown('### Keyword network')
        # Carregar o DataFrame com palavras-chave
        df = st.session_state["Portfolio"]
        # Manter palavras-chave minúsculas e por linhas (granularidade já está em nível de palavra-chave)
        df['keywords'] = df['keywords'].str.lower()
        # Remover palavras-chave que são NaN
        df = df.dropna(subset=['keywords'])

        # Passo 1: Contar as co-ocorrências de palavras-chave
        G = nx.Graph()
        cooccurrence_counts = Counter()
        # Contar co-ocorrências e filtrar palavras-chave mais frequentes
        articles = df.groupby('title')['keywords'].apply(list).reset_index()
        for keywords in articles['keywords']:
            if len(keywords) > 20:  # Garantir que existam palavras-chave suficientes
                for pair in combinations(keywords, 2):  # Combinações de palavras-chave em pares
                    cooccurrence_counts[pair] += 1
        # Filtrar as palavras-chave que ocorrem com mais frequência
        most_common_keywords = [k for k, v in cooccurrence_counts.items() if v > 10]  # Ajuste o limite conforme necessário
        # Adicionar arestas com base nas co-ocorrências filtradas
        for (kw1, kw2), weight in cooccurrence_counts.items():
            if weight > 10:  # Mantém arestas com co-ocorrência significativa
                G.add_edge(kw1, kw2, weight=weight)

        # Passo 2: Clusterizar as palavras-chave usando o algoritmo de Louvain
        partition = community_louvain.best_partition(G)
        
        # Passo 3: Visualizar a rede de palavras-chave com clusters
        plt.figure(figsize=(20, 10))
        # Layout do grafo com maior espaçamento entre os nós
        pos = nx.spring_layout(G, k=8, iterations=100)  # Aumentei o valor de 'k' para maior espaçamento
        node_colors = [partition[node] for node in G.nodes()]

        nx.draw_networkx_nodes(G, pos, node_size=200, cmap=plt.cm.RdYlBu, node_color=node_colors)
        nx.draw_networkx_edges(G, pos, alpha=0.03, width=[G[u][v]['weight']*0.1 for u, v in G.edges()])
        nx.draw_networkx_labels(G, pos, font_size=12)  # Diminui o tamanho da fonte

        st.pyplot(plt)
