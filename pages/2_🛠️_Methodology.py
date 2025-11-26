import streamlit as st # type: ignore
import webbrowser
import pandas as pd # type: ignore

st.header('🛠️ Methodology', divider=True)
# Sumário na Sidebar
section = st.sidebar.radio("**Go to**:", 
                           ["AI-Copiloted SLR",
                            "High Level Workflow", 
                            "1. Keywords definition", 
                            "2. Portfolio Selection", 
                            "3. Portfolio Scanning", 
                            "4. Portfolio Analysis"])

# Título e conteúdo principal
st.markdown(
    "The proposed approach comprises four phases designed to identify, classify, and analyze a portfolio of studies, revealing research profiles and opportunities for future investigation. \n\nTasks are defined according to research needs and supporting tools: (i) manual tasks, conducted in reference managers or analytical environments; (ii) user tasks, performed by researchers in journal databases; (iii) scripts, automated through Python for data processing or searches; (iv) prompts, instructions used to query AI models; and (v) assistant tasks, delegated to AI agents for operations such as filtering or article categorization."
    )

if section == "AI-Copiloted SLR":
    st.markdown("### AI-Copiloted Literature Review")
    st.image("images/AI-ET-Review-FULL.png")

elif section == "High Level Workflow":
    st.markdown("### High Level Workflow")
    st.image("images/_00-AI-ET-Review.png")
    st.divider()

elif section == "1. Keywords definition":
    st.markdown("### 1. Keywords definition")
    st.image("images/_01-Keywords-definition.png")
    st.divider()

elif section == "2. Portfolio Selection":
    st.markdown("### 2. Portfolio Selection")
    st.image("images/_02-Portfolio-selection.png")

    # Configurando layout de duas colunas
    col1, col2 = st.columns(2)
    # Configurando coluna 1
    with col1:
        st.markdown("#### 2.1 Exclude by Journal Impact Factor")
        st.image("images/_02_01-Exclude-by-journal-impact-factor.png")

    # Configurando coluna 2
    with col2:
        st.markdown("#### 2.2 Exclude by Reading Titles and Abstracts")
        st.image("images/_02_02-Exclude-by-reading-titles-and-abstracts.png")
    st.divider()

elif section == "3. Portfolio Scanning":
    st.markdown("### 3. Portfolio Scanning")
    st.image("images/_03-portfolio-scanning.png")
    st.divider()

elif section == "4. Portfolio Analysis":
    st.markdown("### 4. Portfolio Analysis")
    st.image("images/_04-portfolio-analysis.png")