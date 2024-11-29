import streamlit as st
import pandas as pd

st.header("🎲 Database", divider=True)
section = st.sidebar.radio("**Go to**:", 
                           ["Journals Ranking",
                            "Porfolio",
                            "Portfolio Citations",
                            "Porfolio Encoded"])

# Verificar se o portfolio está presente na session_state
if "Portfolio" not in st.session_state and "JIF" not in st.session_state and "Portfolio-citations" not in st.session_state and "encoded-portfolio" not in st.session_state:
    st.error("⚠️ O portfólio não foi carregado. Por favor, volte para a Homepage para carregar os dados.")

else:
    st.markdown("✔️ Portfolio carregado com sucesso!")
    st.divider()

    portfolio = st.session_state["Portfolio"]
    tabela_jif = st.session_state["JIF"]
    portfolio_citations = st.session_state["Portfolio-citations"]
    portfolio_encoded = st.session_state["encoded-portfolio"]
    
    if section == "Journals Ranking":
        st.markdown("## Journals ranking and impact factor")
        tabela_jif["Journal name"] = tabela_jif["Journal name"].str.lower()
        portfolio["journal"] = portfolio["journal"].str.lower()
        tabela_jif_port = tabela_jif[tabela_jif['Journal name'].isin(portfolio['journal'].unique())]
        st.write(tabela_jif_port)
        st.write('Journals count:', tabela_jif_port['Journal name'].count())
    
    elif section == "Porfolio":
        st.markdown("## Article portfolio")
        portfolio["journal"] = portfolio["journal"].str.lower()
        st.write(portfolio)

    elif section == "Portfolio Citations":
        st.markdown("## Portfolio citations")
        st.write(portfolio_citations)
    
    elif section == "Porfolio Encoded":
        st.markdown("## Portfolio encoded")
        st.write(portfolio_encoded)