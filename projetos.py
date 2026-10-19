
import streamlit as st
from pathlib import Path
from PIL import Image, ImageOps

# CONFIGURAÇÕES DOS ARQUIVOS

PASTA_PROJETO = Path(__file__).resolve().parent

IMAGEM_CHATBOT = PASTA_PROJETO / "Chatbot.png"
IMAGEM_ANALISADOR = PASTA_PROJETO / "Analisador.png"
IMAGEM_DIAGNOSTICO = PASTA_PROJETO / "Diagnóstico.png"
IMAGEM_AUTOMATIZADOR = PASTA_PROJETO / "Automatizador.png"
IMAGEM_WIFI = PASTA_PROJETO / "WIFI.png"
IMAGEM_BANNER = PASTA_PROJETO / "banner2.png"
IMAGEM_ESPERAR = PASTA_PROJETO / "Oqueesperardemim_.png"
IMAGEM_DASHBOARD = PASTA_PROJETO / "Dashboard.png"


# FUNÇÃO PARA EXIBIR IMAGENS
def exibir_imagem(caminho, padronizar=False):

    if not caminho.exists():
        st.warning(
            f"Imagem {caminho.name} não encontrada.")
        return

    if padronizar:

        with Image.open(caminho) as original:

            imagem = ImageOps.fit(
                original.convert("RGB"),
                (600, 400),
                method=Image.Resampling.LANCZOS,
                centering=(0.5, 0.5))

        st.image(
            imagem,
            use_container_width=True)

    else:

        st.image(
            str(caminho),
            use_container_width=True)

# FUNÇÃO PRINCIPAL: PROJETOS ACADÊMICOS

def exibir_projetos():
# BOTÃO VOLTAR AO INÍCIO

    if st.button("⬅ Voltar ao início"):
        st.session_state.pagina = "inicio"
        st.rerun()

# BANNER DOS PROJETOS
    exibir_imagem(IMAGEM_BANNER)

    st.divider()

# ESTILO VISUAL
    st.markdown(
        """
        <style>

        .sobre-titulo {
            font-size: 34px;
            font-weight: 750;
            margin-bottom: 8px;
            color: #FFFFFF;}

        .sobre-linha {
            width: 65px;
            height: 4px;
            background: #DC2626;
            border-radius: 10px;
            margin-bottom: 25px;}

        </style>""", unsafe_allow_html=True)

# TÍTULO DOS PROJETOS
    st.markdown(
        '<div class="sobre-titulo">'
        'Projetos Acadêmicos:'
        '</div>'
        '<div class="sobre-linha"></div>',
        unsafe_allow_html=True)

# PRIMEIRA LINHA DE PROJETOS
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:

        st.subheader("Dashboard Acadêmico:")

        st.write(
            "Sistema desenvolvido em Python e Streamlit "
            "para acompanhamento de notas, atividades "
            "e desempenho acadêmico.")

        exibir_imagem(IMAGEM_DASHBOARD, padronizar=True)

        st.link_button("↗ EXPLORAR PROJETO | SITE", "https://dashboard-academico-wenndy.streamlit.app/", use_container_width=True)

    with col2:

        st.subheader("ChatBot com Inteligência Artificial:")

        st.write(
            "Projeto acadêmico desenvolvido em Python "
            "e Streamlit, com integração à API do "
            "Google Gemini para interação com "
            "Inteligência Artificial.")

        exibir_imagem(IMAGEM_CHATBOT, padronizar=True)

        st.link_button("↗ EXPLORAR PROJETO | SITE", "https://chatbotwe.streamlit.app/", use_container_width=True)

    with col3:

        st.subheader("Analisador de Rede Wi-Fi:")

        st.write(
            "Ferramenta desenvolvida em Python para "
            "diagnóstico local de redes sem fio, "
            "consulta de informações e análise "
            "de conectividade no Windows.")

        exibir_imagem(IMAGEM_WIFI, padronizar=True)

        st.link_button("↗ VER CÓDIGO NO GITHUB", "https://github.com/WenndyFerreira/Analisador-de-Redes-Wi-Fi", use_container_width=True)

# ESPAÇAMENTO ENTRE AS LINHAS
    st.write("")
    st.write("")

# SEGUNDA LINHA DE PROJETOS
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:

        st.subheader("Analisador de Logs de Segurança:")

        st.write(
            "Projeto desenvolvido em Python para "
            "análise de registros de autenticação, "
            "identificação de tentativas suspeitas "
            "de acesso e geração de relatórios "
            "de segurança.")

        exibir_imagem(IMAGEM_ANALISADOR, padronizar=True)

        st.link_button("↗ VER CÓDIGO NO GITHUB", "https://github.com/WenndyFerreira/Analisador-de-Logs-de-Seguran-a", use_container_width=True)

    with col2:

        st.subheader("Diagnóstico de Computadores:")

        st.write(
            "Sistema desenvolvido em Python para "
            "consultar informações do sistema operacional, "
            "processador, memória RAM, armazenamento "
            "e interfaces de rede.")

        exibir_imagem(IMAGEM_DIAGNOSTICO, padronizar=True)

        st.link_button("↗ VER CÓDIGO NO GITHUB", "https://github.com/WenndyFerreira/Diagn-stico-de-Computadores", use_container_width=True)

    with col3:

        st.subheader("Automatizador de Relatórios Excel:")

        st.write(
            "Aplicação desenvolvida em Python, Pandas "
            "e OpenPyXL para importar planilhas Excel, "
            "analisar indicadores, identificar "
            "inconsistências e gerar relatórios "
            "formatados automaticamente.")

        exibir_imagem(IMAGEM_AUTOMATIZADOR, padronizar=True)

        st.link_button("↗ VER CÓDIGO NO GITHUB", "https://github.com/WenndyFerreira/Automatizador-de-Relat-rios-Excel", use_container_width=True)

    st.divider()
    
    exibir_imagem(IMAGEM_ESPERAR)

    st.divider()


