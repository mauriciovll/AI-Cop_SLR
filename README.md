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


---

## Project Description
This repository contains all the source code, data and support page for the article *"Emerging & data technologies applied to public sector: an AI-copiloted systematic literature review"*, written by Maurício Vasconcellos Leão Lyrio, Fabrícia Silva da Rosa, Miklos A. Vasarhelyi and Rogério João Lunkes. The web page hosts the tables and visualizations presented in the article, as well as the specialized assistant and can be reused under the MIT license.

## Methodology

The authors propose a systematic process for literature review, co-piloted by artificial intelligence (H. Gu et al., 2024) and inspired by previous studies (Lyrio et al., 2018; Page et al., 2021; Ruijer et al., 2023; Short, 2009; Straub et al., 2023), which seeks to establish an organized flow of activities to generate knowledge on a given topic.

The approach consists of 4 phases that aim to identify a portfolio of studies related to the topic and then classify and analyze them in order to identify the research profile and opportunities for future studies. The figure below presents the workflow and types of tasks involved, providing a clear guide regarding the tasks and responsibilities of each phase of the process.

<p align="center">
<img src="images/AI-ET-Review-FULL.png" alt="imagem">
</p>

The tasks are defined according to the research needs and tools used, as follows:

(i) manual task – tasks performed in a reference manager and/or knowledge-based analytical tasks performed by researchers;

(ii) user task – tasks performed by researchers in journal databases;

(iii) script task – tasks automated through python scripts, used to process data or perform searches;

(iv) prompt task – tasks in which query instructions (prompts) are used to interact with AI models;

(v) assistant task – tasks delegated to AI assistants to perform specific tasks, such as filtering or categorizing articles.

## Installation and use
To use the repository, you must create a virtual environment `python -m venv venv`. Then you must initialize the virtual environment `venv/scripts/activate -> command for windows` and install the dependencies `pip install -r requirements.txt`.

To run the application locally, type the Streamlit initialization command `streamlit run 1_??_home.py`.

You must add credits to your [OpenAI Platform](https://platform.openai.com/docs/overview) account in order to run the assistant. In the settings tab, click on organization > Billing and enter the desired value.

To initialize the Assistant, you must enter the OpenAI API key. To do so, go to [OpenAI Platform](https://platform.openai.com/docs/overview) > Dashboard > API Keys and create a new API key. After creating the key, copy and paste it into the location indicated in the .env file

## Citation

## Contact
Corresponding author: [Maurício Vasconcellos Leão Lyrio](https://br.linkedin.com/in/maurício-vasconcellos-leão-lyrio-59773220)
