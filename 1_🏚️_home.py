import streamlit as st # type: ignore
import webbrowser
import pandas as pd # type: ignore

st.header("📈 Home", divider=True)

# Carregando as tabelas do projeto
if "Portfolio" not in st.session_state and "JIF" not in st.session_state and "Portfolio-citations" not in st.session_state and "encoded-portfolio" not in st.session_state:
    df = pd.read_excel("C:/Users/mauri/OneDrive/Repositorios/AI-Cop_SLR/data/processed/_11_portfolio-135-final.xlsx", index_col=0)
    portfolio = df.sort_values(by="title", ascending=True)
    st.session_state["Portfolio"] = portfolio
    df_jif = pd.read_excel("C:/Users/mauri/OneDrive/Repositorios/AI-Cop_SLR/data/processed/_6_journals-JIF-Q1.xlsx", index_col=0)
    st.session_state["JIF"] = df_jif
    df_port_citation = pd.read_excel("C:/Users/mauri/OneDrive/Repositorios/AI-Cop_SLR/data/processed/_12_portfolio-135-citations.xlsx", index_col=0)
    st.session_state["Portfolio-citations"] = df_port_citation
    df_encoded_portfolio = pd.read_excel("C:/Users/mauri/OneDrive/Repositorios/AI-Cop_SLR/data/processed/_10_encoded-articles-adjusted.xlsx", index_col=0)
    st.session_state["encoded-portfolio"] = df_encoded_portfolio

st.markdown(
        """
        # Emerging & Data Technologies applied to public sector:
        ### an AI-Copiloted Systematic Literature Review Approach
        """
    )
st.divider()

st.markdown(
    """
    #### Abstract:
    """
)

st.markdown(
    """
    ##### Autores:
    [Maurício Vasconcellos Leão Lyrio](https://br.linkedin.com/in/maur%C3%ADcio-vasconcellos-le%C3%A3o-lyrio-59773220), Dr.; Fabrícia Silva da Rosa, Dra.; Miklos Vasarhelyi,  PhD.; Rogério João Lunkes, Dr.
    """
)
st.divider()

# Rodapé
st.markdown("##### Project Repository:")
btn = st.button("Git Hub")
if btn:
    webbrowser.open_new_tab("https://github.com/mauriciovll/AI-Cop_SLR/tree/main")


