import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent # type: ignore
from langchain_openai import ChatOpenAI # type: ignore
import pandas as pd

# Carregar o DataFrame
df = st.session_state["encoded-portfolio"]

# Criar cabeçalho da página
st.header('🤖 Research Assistant', divider=True)
api_key = st.text_input("Insert here your Open AI API Key:", type="password", key="OPENAI_API_KEY")
if not api_key:
    st.info("🔑 Please insert your OpenAI API Key to start using the assistant.")
    st.stop()

# Configurar histórico da sessão
if "historico" not in st.session_state:
    mensagem_inicial = {'role': 'assistant', 'content': 'Hello, I am your research assistant. My role is to support you in the process of analyzing the articles in our article portfolio. Lets get started?'}
    st.session_state.historico = [mensagem_inicial]

# Configurar o modelo de linguagem e o agente
chat = ChatOpenAI(
    model="gpt-5.1",
    openai_api_key=api_key,
    max_tokens=500)
agent = create_pandas_dataframe_agent(
    chat,
    df,
    verbose=True,
    agent_type='tool-calling',
    allow_dangerous_code=True,
    max_iterations=5
)


# Montar o chatbot
for mensagem in st.session_state.historico:
    chat = st.chat_message(mensagem['role'])
    chat.markdown(mensagem['content'])

# Entrada do usuário
prompt = st.chat_input("Ask to assistant:")
if prompt:
    nova_mensagem = {'role': 'user', 'content': prompt}
    st.session_state.historico.append(nova_mensagem)
    st.chat_message(nova_mensagem['role']).markdown(nova_mensagem['content'])

    # Construir o histórico como contexto
    contexto = "\n".join(
        [f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.historico]
    )

    # Adicionar contexto ao prompt
    prompt_completo = f"{contexto}\nAssistant:"
    resposta = agent.run(prompt_completo)

    # Adicionar resposta ao histórico
    nova_resposta = {'role': 'assistant', 'content': resposta}
    st.session_state.historico.append(nova_resposta)
    st.chat_message(nova_resposta['role']).markdown(nova_resposta['content'])
