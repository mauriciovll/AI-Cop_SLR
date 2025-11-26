import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("🔬 Content Analysis", divider=True)
# Sumário na Sidebar
section = st.sidebar.radio("**Go to**:", 
                           ["Methodological Profile",
                            "Thematic Profile",
                            "Technologies discussed"])

portfolio_encoded = st.session_state["encoded-portfolio"]

if section == "Methodological Profile":
    st.markdown("### Methodological Profile")
    
    cols = st.columns(2)
    with cols[0]:  # 1. Research Approach
        st.markdown("##### Research Approach")
        df_ra = portfolio_encoded[['doi_number', 'research_approach']]
        df_ra_counts = df_ra['research_approach'].value_counts().reset_index()
        df_ra_counts.columns = ['Research Approach', 'Ocurrences']
        st.write(df_ra_counts)

    with cols[1]:
        plt.figure(figsize=(6, 2))
        df_ra_top5 = df_ra_counts.head(5)
        sns.barplot(y='Research Approach', x='Ocurrences', data=df_ra_top5, palette='viridis')
        plt.title('Research Approaches', fontsize=10)
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(plt)

    st.divider()

    cols = st.columns(2)
    with cols[0]:  # 2. Research Methods
        st.markdown("##### Research Methods")
        df_rm = portfolio_encoded[['doi_number', 'research_method']]
        df_rm_counts = df_rm['research_method'].value_counts().reset_index()
        df_rm_counts.columns = ['Research Method', 'Ocurrences']
        st.write(df_rm_counts)    

    with cols[1]:
        plt.figure(figsize=(6, 2))
        df_rm_top5 = df_rm_counts.head(5)
        sns.barplot(y='Research Method', x='Ocurrences', data=df_rm_top5, palette='viridis')
        plt.title('Top 5 Research Methods', fontsize=10)
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(plt)    
        
    st.divider()

    col1, col2 = st.columns(2)  
    with col1:  # 3. Analysis Techniques
        st.markdown("##### Analysis Techniques")
        df_at = portfolio_encoded[['doi_number', 'analysis_techniques']]
        df_at_exp1 = df_at.assign(analysis_techniques=df_at['analysis_techniques'].str.split(';')).explode('analysis_techniques')
        df_at_exp2 = df_at_exp1.assign(analysis_techniques=df_at_exp1['analysis_techniques'].str.split(',')).explode('analysis_techniques')
        df_at_exp2['analysis_techniques'] = df_at_exp2['analysis_techniques'].str.strip()
        df_at_counts = df_at_exp2['analysis_techniques'].value_counts().reset_index()
        df_at_counts.columns = ['Analysis Techniques', 'Ocurrences'] 
        st.write(df_at_counts)        

    with col2:
        plt.figure(figsize=(6, 2))
        df_at_top5 = df_at_counts.head(5)
        sns.barplot(y='Analysis Techniques', x='Ocurrences', data=df_at_top5, palette='viridis')
        plt.title('Top 5 Analysis Techniques', fontsize=10)
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(plt)    
        
    st.divider()

    col1, col2 = st.columns(2)
    with col1:  # 4. Theoretical background
        st.markdown("##### Theoretical background")
        df_tb = portfolio_encoded[['doi_number', 'theoretical_background']]
        df_tb_exp1 = df_tb.assign(theoretical_background=df_tb['theoretical_background'].str.split(';')).explode('theoretical_background')
        df_tb_exp2 = df_tb_exp1.assign(theoretical_background=df_tb_exp1['theoretical_background'].str.split(',')).explode('theoretical_background')
        df_tb_exp2['theoretical_background'] = df_tb_exp2['theoretical_background'].str.strip()
        df_tb_counts = df_tb_exp2['theoretical_background'].value_counts().reset_index()
        df_tb_counts.columns = ['Theoretical Background', 'Ocurrences']
        st.write(df_tb_counts)        

    with col2:
        plt.figure(figsize=(6, 2))
        df_tb_top5 = df_tb_counts.head(5)
        sns.barplot(y='Theoretical Background', x='Ocurrences', data=df_tb_top5, palette='viridis')
        plt.title('Top 5 theoretical background', fontsize=10)
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(plt)        
        
    st.divider()

if section == "Thematic Profile":
    st.markdown("### Thematic Profile")
    col1, col2 = st.columns(2)
    with col1:  # 1. Analysis Level
        st.markdown("##### Analysis level")
        df_al = portfolio_encoded[['doi_number', 'analysis_level']]
        df_al_counts = df_al['analysis_level'].value_counts().reset_index()
        df_al_counts.columns = ['Analysis Level', 'Ocurrences']
        st.write(df_al_counts)

    with col2:
        plt.figure(figsize=(6, 2))
        df_al_top5 = df_al_counts.head(5)
        sns.barplot(y='Analysis Level', x='Ocurrences', data=df_al_top5, palette='viridis')
        plt.title('Analysis Level', fontsize=10)
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(plt)        
        
    st.divider()

    col1, col2 = st.columns(2)  
    with col1:  # 2. Research Topic
        st.markdown("##### Research Topics")
        df_rt = portfolio_encoded[['doi_number', 'research_topics']]
        df_rt_counts = df_rt['research_topics'].value_counts().reset_index()
        df_rt_counts.columns = ['Research Topics', 'Ocurrences']
        st.write(df_rt_counts)

    with col2:
        plt.figure(figsize=(6, 2))
        df_rt_top5 = df_rt_counts.head(5)
        sns.barplot(y='Research Topics', x='Ocurrences', data=df_rt_top5, palette='viridis')
        plt.title('Top 5 research topics', fontsize=10)
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(plt)        
        
    st.divider()

    col1, col2 = st.columns(2)
    with col1: # 3. Research Context
        st.markdown("##### Research Context")
        df_rc = portfolio_encoded[['doi_number', 'research_context']]
        df_rc_exp1 = df_rc.assign(research_context=df_rc['research_context'].str.split('/')).explode('research_context')
        df_rc_exp1['research_context'] = df_rc_exp1['research_context'].str.strip()
        df_rc_counts = df_rc_exp1['research_context'].value_counts().reset_index()
        df_rc_counts.columns = ['Research Context', 'Ocurrences']
        st.write(df_rc_counts)

    with col2:
        plt.figure(figsize=(6, 2))
        df_rc_top5 = df_rc_counts.head(5)
        sns.barplot(y='Research Context', x='Ocurrences', data=df_rc_top5, palette='viridis')
        plt.title('Top 5 research context', fontsize=10)
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(plt)

    st.divider()    
    
    col1, col2 = st.columns(2)
    with col1:  # 4. Geographical Context
        st.markdown("##### Geographical Context")
        df_gc = portfolio_encoded[['doi_number', 'geographical_context']]
        df_gc_counts = df_gc['geographical_context'].value_counts().reset_index()
        df_gc_counts.columns = ['Geographical Context', 'Ocurrences']
        st.write(df_gc_counts)

    with col2:
        plt.figure(figsize=(6, 2))
        df_gc_top5 = df_gc_counts.head(5)
        sns.barplot(y='Geographical Context', x='Ocurrences', data=df_gc_top5, palette='viridis')
        plt.title('Top 5 geographical context', fontsize=10)
        plt.xlabel('Ocurrences')
        plt.ylabel(None)
        st.pyplot(plt)
    
    st.divider()

    col1, col2 = st.columns(2)
    with col1:  # 5. Government Level
        st.markdown("##### Government Level")
        df_gl = portfolio_encoded[['doi_number', 'government_level']]
        df_gl_counts = df_gl['government_level'].value_counts().reset_index()
        df_gl_counts.columns = ['Government Level', 'Ocurrences']
        st.write(df_gl_counts)
    
    with col2:
        plt.figure(figsize=(6, 2))
        df_gl_top5 = df_gl_counts.head(5)
        sns.barplot(y='Government Level', x='Ocurrences', data=df_gl_top5, palette='viridis')
        plt.title('Government Level', fontsize=10)
        plt.xlabel('Ocurrences')
        plt.ylabel(None)
        st.pyplot(plt)

    st.divider()

if section == "Technologies discussed":
    col1, col2 = st.columns(2)        
    with col1:   # Technology Discussed
        df_td = portfolio_encoded[['doi_number', 'technology_discussed']]
        df_td_exp1 = df_td.assign(technology_discussed=df_td['technology_discussed'].str.split(';')).explode('technology_discussed')
        df_td_exp1['technology_discussed'] = df_td_exp1['technology_discussed'].str.strip()
        df_td_counts = df_td_exp1['technology_discussed'].value_counts().reset_index()
        df_td_counts.columns = ['Technology Discussed', 'Ocurrences']
        st.write(df_td_counts)

    with col2:         
        plt.figure(figsize=(6, 2))
        df_td_top5 = df_td_counts.head(5)
        sns.barplot(y='Technology Discussed', x='Ocurrences', data=df_td_top5, palette='viridis')
        plt.title('Top 5 technologies discussed', fontsize=10)
        plt.xlabel('Ocurrences')
        plt.ylabel(None)
        st.pyplot(plt)

    st.divider()