import streamlit as st
from pathlib import Path
from PIL import Image, ImageOps
from experiencias import exibir_experiencias
from projetos import exibir_projetos
from MinhasCompetências import exibir_competencias
from Certificados import exibir_certificados

# CONFIGURAÇÕES DA PÁGINA
PASTA_PROJETO = Path(__file__).resolve().parent

FOTO = PASTA_PROJETO / "CapturaWenndy.png"

IMAGEM_CHATBOT = PASTA_PROJETO / "Chatbot.png"
IMAGEM_ANALISADOR = PASTA_PROJETO / "Analisador.png"
IMAGEM_DIAGNOSTICO = PASTA_PROJETO / "Diagnóstico.png"
IMAGEM_AUTOMATIZADOR = PASTA_PROJETO / "Automatizador.png"
IMAGEM_WIFI = PASTA_PROJETO / "WIFI.png"

st.set_page_config(page_title="Wenndy Ferreira | Portfólio", page_icon=str(FOTO) if FOTO.exists() else "💻", layout="wide")

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

#FUNÇÃO PARA EXIBIR IMAGENS
def exibir_imagem(caminho, padronizar=False):

    if caminho.exists():
        if padronizar:
            with Image.open(caminho) as original:
                imagem = ImageOps.fit(
                    original.convert("RGB"),
                    (600, 400),
                    method=Image.Resampling.LANCZOS,
                    centering=(0.5, 0.5))

            st.image(imagem, use_container_width=True)

        else:
            st.image(str(caminho), use_container_width=True)

    else:
        st.warning(f"Imagem {caminho.name} não encontrada.")


st.markdown("""
<div style="
    text-align: center;
    color: #A0A0A0;
    font-size: 13px;
    padding: 15px;
    width: 100%;">
    Portfólio
</div>""", unsafe_allow_html=True)

#INICIAL
if st.session_state.pagina == "inicio":

    st.image("banner.png", use_container_width=True)

    st.divider()

    st.markdown("""
    <style>
    .sobre-titulo {
        font-size: 34px;
        font-weight: 750;
        margin-bottom: 8px;}

    .sobre-linha {
        width: 65px;
        height: 4px;
        background: #DC2626;
        border-radius: 10px;
        margin-bottom: 25px;}

    .sobre-texto {
        font-size: 16px;
        line-height: 1.9;
        color: inherit;
        margin-bottom: 18px;}

    .sobre-destaque {
        font-weight: 700;
        color: #DC2626;}
    </style>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="sobre-titulo">Sobre mim:</div>
    <div class="sobre-linha"></div>

    <p class="sobre-texto">
    Olá! Meu nome é <span class="sobre-destaque">Wenndy Ferreira dos Santos</span>,
    nascido em 1997 e atualmente resido em
    <strong>Itaquera, SP</strong>. Sou um profissional dedicado,
    organizado e comprometido com meu desenvolvimento pessoal
    e profissional. Desde 2019, venho construindo minha trajetória
    no mercado de trabalho, adquirindo experiências em diferentes
    ambientes corporativos e desenvolvendo habilidades que
    contribuem para minha evolução contínua.
    </p>

    <p class="sobre-texto">
    Minha trajetória profissional é construída principalmente nas
    <strong>áreas administrativa, operacional e de relacionamento
    com clientes</strong>. Ao longo dos anos, tive a oportunidade
    de atuar em empresas de diferentes segmentos, ampliando
    minha visão sobre processos organizacionais, rotinas
    corporativas, comunicação entre equipes e atendimento
    às necessidades operacionais.
    </p>

    <p class="sobre-texto">
    Durante essa trajetória, desenvolvi experiência em
    <strong>rotinas administrativas, BackOffice, organização
    e acompanhamento de demandas, elaboração de relatórios,
    análise de informações, suporte operacional e resolução
    de problemas</strong>. Essas atividades fortaleceram
    minha capacidade de organização, pensamento analítico,
    comunicação profissional e adaptação a diferentes
    sistemas e metodologias de trabalho.
    </p>

    <p class="sobre-texto">
    Atualmente, sou estudante de
    <span class="sobre-destaque">Análise e Desenvolvimento de
    Sistemas pela Universidade Anhanguera</span>,
    formação que representa uma importante etapa da minha
    evolução profissional. Meu interesse pela tecnologia
    está relacionado à possibilidade de desenvolver soluções,
    automatizar atividades, interpretar dados e utilizar
    ferramentas digitais para tornar processos mais
    eficientes e inteligentes.
    </p>

    <p class="sobre-texto">
    Possuo conhecimentos em
    <strong>Pacote Office avançado, Power BI e análise
    de dados</strong>, ferramentas que complementam minha
    experiência administrativa e contribuem para umaatuação
    mais estratégica, especialmente na organização de
    informações, construção de relatórios e acompanhamento
    de indicadores.
    </p>

    <p class="sobre-texto">
    Na área de Tecnologia da Informação, venho aprofundando
    meus estudos em <strong>programação Python, lógica de
    programação, desenvolvimento de software, bancos de dados,
    redes de computadores, automação de processos e fundamentos
    de segurança da informação</strong>. Busco transformar
    o conhecimento adquirido durante minha formação em
    experiências práticas e projetos que contribuam
    para meu desenvolvimento técnico.
    </p>

    <p class="sobre-texto">
    Como parte desse aprendizado, desenvolvo
    <strong>projetos acadêmicos e aplicações práticas
    utilizando Python, Streamlit, Pandas e OpenPyXL</strong>,
    explorando recursos de análise de dados, criação de
    dashboards interativos, automação de relatórios,
    desenvolvimento de sistemas e integração com
    Inteligência Artificial.
    </p>

    <p class="sobre-texto">
    Acredito que meu principal diferencial está na
    <span class="sobre-destaque">combinação entre experiência
    administrativa e conhecimentos tecnológicos</span>.
    Essa integração me permite compreender necessidades
    operacionais, identificar oportunidades de melhoria
    e buscar soluções que contribuam para a produtividade,
    organização e eficiência dos processos.
    </p>

    <p class="sobre-texto">
    Sou movido pelo aprendizado contínuo, pela curiosidade
    e pela vontade de evoluir profissionalmente. Valorizo
    a responsabilidade, a colaboração, a comunicação clara
    e o compromisso com a qualidade do trabalho.
    Meu propósito é continuar construindo uma trajetória
    sólida, contribuindo com minhas experiências e
    desenvolvendo novas competências nas áreas
    <strong>Administrativa e de Tecnologia da Informação</strong>.
    </p>
    """, unsafe_allow_html=True)

    st.divider()

# EXPERIÊNCIA PROFISSIONAL
# CONECTADA AO ARQUIVO experiencias.py

    exibir_experiencias()

    st.divider()

# MINHAS COMPETÊNCIAS
    exibir_competencias()

    st.divider()

#CERTIFICADOS   
    exibir_certificados()

    st.divider()

# PROJETOS ACADÊMICOS
    st.header("Projetos Acadêmicos:")

    st.write(
        "Conheça os projetos que desenvolvi durante "
        "minha formação em Análise e Desenvolvimento "
        "de Sistemas, utilizando Python, Streamlit, "
        "Pandas e outras tecnologias.")

    if st.button(
        "Ver Projetos Acadêmicos",
        type="primary",
        use_container_width=True):
        st.session_state.pagina = "projetos"
        st.rerun()
    
elif st.session_state.pagina == "projetos":
    exibir_projetos()


# CONTATOS
col1, col2, col3, col4 = st.columns(4, gap="medium")

with col1:
    st.subheader("LinkedIn:")

    st.link_button(
        "🔗 Acessar LinkedIn",
        "https://www.linkedin.com/in/wenndy-ferreira-875a32251", use_container_width=True)

with col2:
    st.subheader("GitHub:")

    st.link_button(
        "💻 Acessar GitHub",
        "https://github.com/WenndyFerreira", use_container_width=True)

with col3:
    st.subheader("E-mail:")

    st.link_button(
        "✉️ Enviar e-mail",
        "mailto:Wenndyferreira45@gmail.com", use_container_width=True)

with col4:
    st.subheader("Telefone:")

    st.link_button(
        "📞 Ligar",
        "tel:+5511991356877",
        use_container_width=True)

st.divider()

# RODAPÉ
st.markdown("""
<div style="
    text-align: center;
    color: #A0A0A0;
    font-size: 13px;
    padding: 15px;
    width: 100%;">
    © 2026 Wenndy Ferreira dos Santos |
    Portfólio Profissional e Acadêmico |
    Desenvolvido com Python e Streamlit
</div>""", unsafe_allow_html=True)
