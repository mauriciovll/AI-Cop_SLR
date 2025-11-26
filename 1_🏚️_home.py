import streamlit as st # type: ignore
import webbrowser
import pandas as pd # type: ignore

st.header("📈 Home", divider=True)

# Carregando as tabelas do projeto
if "Portfolio" not in st.session_state and "JIF" not in st.session_state and "Portfolio-citations" not in st.session_state and "encoded-portfolio" not in st.session_state:
    df = pd.read_excel("data/processed/_11_portfolio-135-final.xlsx", index_col=0)
    portfolio = df.sort_values(by="title", ascending=True)
    st.session_state["Portfolio"] = portfolio
    df_jif = pd.read_excel("data/processed/_6_journals-JIF-Q1.xlsx", index_col=0)
    st.session_state["JIF"] = df_jif
    df_port_citation = pd.read_excel("data/processed/_12_portfolio-135-citations.xlsx", index_col=0)
    st.session_state["Portfolio-citations"] = df_port_citation
    df_encoded_portfolio = pd.read_excel("data/processed/_10_encoded-articles-adjusted.xlsx", index_col=0)
    st.session_state["encoded-portfolio"] = df_encoded_portfolio

st.markdown(
    """
    # Emerging & Data Technologies applied to public sector:
    ### an AI-Copiloted Systematic Literature Review Approach
    """
)

st.markdown(
    """
    This study aimed to explore the use of emerging and data technologies (Rotolo et al., 2015) in the public sector, investigating their applications, challenges, and benefits through the analytical perspectives proposed by Criado et al. (2024). To amplify the analytical capacity, minimize data processing time and analyze relevant studies on the topic in high-impact journals, the study adopts a systematic literature review process, inspired by H. Gu’s et al. (2024) co-piloted artificial intelligence (AI) in audit studies and informed by prior literature review methods (Lyrio et al., 2018; Page et al., 2021; Ruijer et al., 2023; Straub et al., 2023). Based on Criado’s et al. (2024) perspectives, the results showed that, at a macro level, AI and big data stand out in the formulation of public policies. At a meso level, use cases demonstrated the potential of these technologies to optimize processes and improve organizational efficiency. At a micro level, the studies highlighted the personalization of public services and improvements in interaction with citizens, although they also warned of risks such as digital exclusion and loss of trust in governments. The study concludes that research on the topic is still in an evolving phase and has prioritized ethical and regulatory issues to balance efficiency, innovation, and the democratic values of the public sector.
    
    \n***Keywords:*** emerging technologies; artificial intelligence; big data; public sector; systematic literature review.
    """
)
st.divider()

st.markdown(
    """
    ##### Authors:
    Maurício Vasconcellos Leão Lyrio; Rogério João Lunkes; Miklos Vasarhelyi.
    """
)

# Rodapé
cols = st.columns(4)
with cols[0]:
    btn_repo = st.button("Git Hub Repository")
    if btn_repo:
        st.page_link("https://github.com/mauriciovll/AI-Cop_SLR/tree/main", label="repositorio")

with cols[1]:
    btn_article = st.button("Article page")
    if btn_article:
        st.page_link("https://revistas.pucp.edu.pe/index.php/contabilidadyNegocios/article/view/32270", label="Article")

with cols[2]:
    pass
with cols[3]:
    pass

