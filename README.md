# Co-piloted Sistematic Literature Review - COP-SLR 1.0

## Descrição do projeto
Este repositório contém todo o código-fonte, dados e página de suporte ao artigo *"Emerging & data technologies applied to public sector: an AI-copiloted systematic literature review"*, escrito por Maurício Vasconcellos Leão Lyrio, Fabrícia Silva da Rosa, Miklos A. Vasarhelyi e Rogério João Lunkes. A página web hospeda as tabelas e visualizações apresentadas no artigo, bem como o assistant especializado e deve ser reutilizada sob a licença MIT.

## Metodologia

Os autores propõem de um processo sistemático para revisão de literatura, co-pilotado por inteligência artificial (H. Gu et al., 2024) e inspirado em estudos anteriores (Lyrio et al., 2018; Page et al., 2021; Ruijer et al., 2023; Short, 2009; Straub et al., 2023), que busca estabelecer um fluxo organizado de atividades para geração de conhecimento sobre determinado tema.

A abordagem é composta por 4 fases que visam identificar um portfolio de estudos relacionados ao tema e posteriormente classificá-los e analisá-los a fim de identificar o perfil da pesquisa e as oportunidades para estudos futuros. A figura abaixo apresenta o fluxo de trabalho e tipos de tarefas envolvidas, fornecendo um guia claro referente as tarefas e responsabilidades de cada fase do processo.

<p align="center">
  <img src="images/AI-ET-Review-FULL.png" alt="imagem">
</p>

As tarefas são definidos de acordo com as necessidades da pesquisa e ferramentas utilizadas, conforme a seguir:
(i) manual task – tarefas realizadas em gerenciador de referências e/ou tarefas analíticas baseadas em conhecimento realizadas pelos pesquisadores;

(ii) user task – tarefas realizadas pelos pesquisadores em bases de dados de periódicos;

(iii) script task – tarefas automatizadas por meio de scripts python, usadas para processar dados ou realizar buscas;

(iv) prompt task – tarefas nas quais instruções de consulta (prompts) são utilizados para interação com modelos de IA;

(v) assistant task – tarefas delegadas a assistentes de IA, para realização de tarefas específicas, como filtragem ou categorização de artigos.

## Instalação e uso
Para utilizar o repositório, você deve criar um ambiente virtual `python -m venv venv`. Em seguida é necessário inicializar o ambiente virtual `venv/scripts/activate -> comando para windows` e instalar as dependências `pip install -r requirements.txt`.

Para rodar a aplicação localmente digitar o comando de inicialização do Streamlit `streamlit run 1_??_home.py`.

É preciso colocar créditos na conta da [OpenAI Platform](https://platform.openai.com/docs/overview) para que seja possível rodar o assistant. Na aba de configurações clicar em organization > Billing e inserir o valor desejado.

Para inicializar o Assistant é preciso inserir a chave de API da OpenAI. Para tanto, acessar [OpenAI Platform](https://platform.openai.com/docs/overview) > Dashboard > API Keys e criar uma nova chave de API. Após criar a chave, copiar e colar no local indicado no arquivo .env

## Citação

## Contato
Corresponding author: [Maurício Vasconcellos Leão Lyrio](https://br.linkedin.com/in/maurício-vasconcellos-leão-lyrio-59773220)

