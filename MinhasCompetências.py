
import streamlit as st
from html import escape

# DADOS DAS COMPETÊNCIAS
competencias = [
        {"titulo": "Inteligência Artificial (IA)",
        "icone": "🧬",
        "habilidades": [
            ("✓", "Desenvolvimento de aplicações com Inteligência Artificial."),
             ("✓", "Integração de modelos de IA por meio de APIs."),
            ("✓", "Criação de chatbots e assistentes virtuais inteligentes."),
            ("✓", "- Automação de processos utilizando Inteligência Artificial.")]},

       {"titulo": "Análise de Dados",
        "icone": "🗄️",
        "habilidades": [
            ("✓", "Tratamento e análise de dados"),
            ("✓", "Visualização de informações"),
            ("✓", "Construção de relatórios"),
            ("✓", "Suporte na tomada de decisões")]},

       {"titulo": "Desenvolvimento de Software",
        "icone": "🧩",
        "habilidades": [
            ("✓", "Lógica de programação"),
            ("✓", "Desenvolvimento de projetos"),
            ("✓", "Criação de interfaces"),
            ("✓", "Boas práticas e versionamento")]},

       {"titulo": "Segurança da Informação",
        "icone": "🛡️",
        "habilidades": [
            ("✓", "Conceitos de segurança"),
            ("✓", "Redes e infraestrutura"),
            ("✓", "LGPD e conformidade"),
            ("✓", "Gestão de riscos")]},

       {"titulo": "Desenvolvimento de Dashboards",
        "icone": "📉",
        "habilidades": [
            ("✓", "Criação de dashboards interativos."),
             ("✓", "Desenvolvimento de indicadores de desempenho (KPIs)."),
            ("✓", "Tratamento e visualização de dados."),
            ("✓", "Elaboração de relatórios gerenciais e analíticos.")]},

       {"titulo": "Automação de Sistemas e Processos",
        "icone": "🔧",
        "habilidades": [
            ("✓", "Desenvolvimento de automações com Python."),
             ("✓", "Automatização de relatórios e planilhas."),
            ("✓", "Integração e processamento de dados."),
            ("✓", "Otimização de processos e tarefas repetitivas.")]},

        {"titulo": "Administrativo",
        "icone": "💼",
        "habilidades": [
            ("✓", "Organização de processos"),
            ("✓", "Gestão de demandas"),
            ("✓", "Comunicação eficiente"),
            ("✓", "Elaboração de relatórios")]},

       {"titulo": "Gestão de Equipes e Comunicação Profissional",
        "icone": "👥",
        "habilidades": [
            ("✓", "Condução de reuniões e alinhamentos de equipe."),
             ("✓", "Aplicação e recebimento de feedbacks construtivos."),
            ("✓", "Comunicação assertiva e relacionamento interpessoal."),
            ("✓", "Acompanhamento de desempenho e desenvolvimento de equipes.")]},

       {"titulo": "Banco de Dados e SQL",
        "icone": "🗃️",
        "habilidades": [
            ("✓", "Modelagem e organização de bancos de dados."),
             ("✓", "Consultas e manipulação de dados com SQL."),
            ("✓", "Estruturação e relacionamento entre tabelas."),
            ("✓", "Integração de bancos de dados com aplicações Python.")]},

       {"titulo": "Programação Python",
        "icone": "🐍",
        "habilidades": [
            ("✓", "Desenvolvimento de scripts e aplicações em Python."),
             ("✓", "Manipulação de dados com Pandas."),
            ("✓", "Programação orientada a objetos."),
            ("✓", "Tratamento de erros e organização de código.")]},

       {"titulo": "Desenvolvimento de Aplicações Web",
        "icone": "🌐",
        "habilidades": [
            ("✓", "Desenvolvimento de aplicações interativas com Streamlit."),
             ("✓", "Criação de interfaces e formulários."),
            ("✓", "Integração de aplicações com APIs."),
            ("✓", "Publicação e disponibilização de projetos na web.")]},

       {"titulo": "Versionamento e Gestão de Projetos",
        "icone": "🔀",
        "habilidades": [
            ("✓", "Controle de versões com Git."),
             ("✓", "Organização de repositórios no GitHub."),
            ("✓", "Documentação técnica de projetos."),
            ("✓", "Planejamento e acompanhamento de atividades.")]}]

# FUNÇÃO PRINCIPAL
def exibir_competencias():

# ESTILO VISUAL
    st.markdown("""<style>

    .comp-cabecalho {
        margin-top: 15px;
        margin-bottom: 30px;}

    .comp-traco-superior {
        width: 65px;
        height: 3px;
        background: #B91C1C;
        margin-bottom: 20px;
        border-radius: 10px;}

    .comp-titulo-leve {
        font-size: 38px;
        font-weight: 300;
        color: #FFFFFF;
        line-height: 1.1;}

    .comp-titulo-forte {
        font-size: 52px;
        font-weight: 800;
        color: #FFFFFF;
        line-height: 1.15;
        margin-bottom: 20px;}

    .comp-descricao {
        color: #D9DDE3;
        font-size: 16px;
        line-height: 1.8;
        max-width: 900px;
        margin-bottom: 25px;}

    .comp-linha {
        width: 65px;
        height: 3px;
        background: #B91C1C;
        border-radius: 10px;}

    .comp-card {
        background: linear-gradient(
            145deg, #1B1B1B, #101010);
        border: 1px solid #383838;
        border-radius: 16px;
        padding: 24px;
        min-height: 410px;
        margin-bottom: 20px;
        transition: 0.3s ease;}

    .comp-card:hover {
        border-color: #B91C1C;
        transform: translateY(-4px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.35);}

    .comp-icone {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 65px;
        height: 65px;
        background: #282828;
        border: 1px solid #555555;
        border-radius: 14px;
        font-size: 30px;
        margin-bottom: 20px;}

    .comp-card-titulo {
        color: #FFFFFF;
        font-size: 21px;
        font-weight: 800;
        line-height: 1.3;
        min-height: 60px;
        margin-bottom: 12px;}

    .comp-divisor {
        height: 1px;
        background: #444444;
        margin-bottom: 18px;}

    .comp-habilidade {
        display: flex;
        align-items: flex-start;
        gap: 10px;
        color: #E5E7EB;
        font-size: 14px;
        line-height: 1.5;
        margin-bottom: 17px;}

    .comp-habilidade-icone {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        width: 30px;
        height: 30px;
        background: #292929;
        border: 1px solid #414141;
        border-radius: 8px;
        color: #F87171;
        font-weight: 700;}

    .comp-habilidade-texto {
        padding-top: 4px;}

    .comp-card-linha {
        width: 55px;
        height: 3px;
        background: #B91C1C;
        border-radius: 10px;
        margin-top: 20px;}

    @media (max-width: 768px) {.comp-titulo-leve {font-size: 30px;}

        .comp-titulo-forte {font-size: 40px;}

        .comp-card {min-height: auto;}}

    </style>""", unsafe_allow_html=True)
    
# CABEÇALHO
    html_cabecalho = (
        '<div class="comp-titulo-leve">'
        'Conhecimentos'
        '</div>'

        '<div class="comp-titulo-forte">'
        'Técnicos:'
        '</div>'

        '<div class="comp-descricao">'
        'Desenvolvi um conjunto de habilidades em diferentes '
        'áreas, unindo experiência prática e aprendizado '
        'contínuo para entregar resultados, resolver problemas '
        'e contribuir com projetos de forma eficiente.'
        '</div>'

        '<div class="comp-linha"></div>'
        '</div>')

    st.markdown(html_cabecalho, unsafe_allow_html=True)

# CARDS DAS COMPETÊNCIAS
    colunas = st.columns(4, gap="medium")

    for indice, competencia in enumerate(competencias):

        habilidades_html = "".join(
            '<div class="comp-habilidade">'
            f'<span class="comp-habilidade-icone">{escape(icone)}</span>'
            f'<span class="comp-habilidade-texto">{escape(texto)}</span>'
            '</div>'
            for icone, texto in competencia["habilidades"])

        html_card = (
            '<div class="comp-card">'

            f'<div class="comp-icone">'
            f'{escape(competencia["icone"])}'
            '</div>'

            f'<div class="comp-card-titulo">'
            f'{escape(competencia["titulo"])}'
            '</div>'

            '<div class="comp-divisor"></div>'

            f'{habilidades_html}'

            '<div class="comp-card-linha"></div>'

            '</div>')

        with colunas[indice % 4]:
            st.markdown(
                html_card,
                unsafe_allow_html=True)
