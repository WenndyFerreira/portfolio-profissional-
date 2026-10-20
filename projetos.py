from html import escape
from pathlib import Path
import streamlit as st
from PIL import Image, ImageOps

# CONFIGURAÇÃO
PASTA_PROJETO = Path(__file__).resolve().parent

IMAGEM_BANNER = PASTA_PROJETO / "banner2.png"
IMAGEM_ESPERAR = PASTA_PROJETO / "Oqueesperardemim_.png"

TAMANHO_MINIATURA = (600, 400)
COLUNAS_POR_LINHA = 3

# Cores do tema
COR_DESTAQUE = "#DC2626"
COR_TEXTO = "#F4F4F5"
COR_TEXTO_SUAVE = "#A1A1AA"
COR_BORDA = "rgba(255, 255, 255, 0.10)"
COR_BORDA_HOVER = "rgba(220, 38, 38, 0.60)"
COR_FUNDO_CARD = "rgba(255, 255, 255, 0.03)"

# Cada projeto é um dicionário: para adicionar ou remover, edite só esta lista.
PROJETOS = [
    {
        "titulo": "Dashboard Acadêmico",
        "descricao": (
            "Sistema para acompanhamento de notas, atividades "
            "e desempenho acadêmico, com indicadores visuais."
        ),
        "tecnologias": ["Python", "Streamlit"],
        "imagem": PASTA_PROJETO / "Dashboard.png",
        "botao": "Ver site",
        "link": "https://dashboard-academico-wenndy.streamlit.app/",
    },
    {
        "titulo": "ChatBot com Inteligência Artificial",
        "descricao": (
            "Chatbot integrado à API do Google Gemini para "
            "conversas com Inteligência Artificial."
        ),
        "tecnologias": ["Python", "Streamlit", "Gemini API"],
        "imagem": PASTA_PROJETO / "Chatbot.png",
        "botao": "Ver site",
        "link": "https://chatbotwe.streamlit.app/",
    },
    {
        "titulo": "Analisador de Rede Wi-Fi",
        "descricao": (
            "Ferramenta para diagnóstico local de redes sem fio, "
            "consulta de informações e análise de conectividade no Windows."
        ),
        "tecnologias": ["Python", "Redes", "Windows"],
        "imagem": PASTA_PROJETO / "WIFI.png",
        "botao": "Ver código no GitHub",
        "link": "https://github.com/WenndyFerreira/Analisador-de-Redes-Wi-Fi",
    },
    {
        "titulo": "Analisador de Logs de Segurança",
        "descricao": (
            "Análise de registros de autenticação para identificar "
            "tentativas suspeitas de acesso e gerar relatórios de segurança."
        ),
        "tecnologias": ["Python", "Segurança", "Logs"],
        "imagem": PASTA_PROJETO / "Analisador.png",
        "botao": "Ver código no GitHub",
        "link": "https://github.com/WenndyFerreira/Analisador-de-Logs-de-Seguran-a",
    },
    {
        "titulo": "Diagnóstico de Computadores",
        "descricao": (
            "Consulta informações do sistema operacional, processador, "
            "memória RAM, armazenamento e interfaces de rede."
        ),
        "tecnologias": ["Python", "Hardware", "Sistema"],
        "imagem": PASTA_PROJETO / "Diagnóstico.png",
        "botao": "Ver código no GitHub",
        "link": "https://github.com/WenndyFerreira/Diagn-stico-de-Computadores",
    },
    {
        "titulo": "Automatizador de Relatórios Excel",
        "descricao": (
            "Importa planilhas, analisa indicadores, identifica "
            "inconsistências e gera relatórios formatados automaticamente."
        ),
        "tecnologias": ["Python", "Pandas", "OpenPyXL"],
        "imagem": PASTA_PROJETO / "Automatizador.png",
        "botao": "Ver código no GitHub",
        "link": "https://github.com/WenndyFerreira/Automatizador-de-Relat-rios-Excel",
    },
]

# ---------------------------------------------------------------------------
# ESTILO
# ---------------------------------------------------------------------------

CSS = f"""
<style>
    .pagina-titulo {{
        font-size: 2.2rem;
        font-weight: 750;
        line-height: 1.15;
        color: {COR_TEXTO};
        margin: 0 0 0.4rem 0;
    }}

    .pagina-linha {{
        width: 64px;
        height: 4px;
        background: {COR_DESTAQUE};
        border-radius: 999px;
        margin-bottom: 0.9rem;
    }}

    .pagina-subtitulo {{
        max-width: 62ch;
        color: {COR_TEXTO_SUAVE};
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 1.8rem;
    }}

    /* Card do projeto: o container recebe a key "card_<n>" */
    [class*="st-key-card_"] {{
        background: {COR_FUNDO_CARD};
        border: 1px solid {COR_BORDA};
        border-radius: 14px;
        padding: 1.1rem 1.1rem 1rem 1.1rem;
        transition: border-color 0.2s ease;
    }}

    [class*="st-key-card_"]:hover {{
        border-color: {COR_BORDA_HOVER};
    }}

    [class*="st-key-card_"] img {{
        border-radius: 10px;
    }}

    .card-titulo {{
        font-size: 1.2rem;
        font-weight: 700;
        line-height: 1.3;
        color: {COR_TEXTO};
        margin: 0.9rem 0 0.4rem 0;
        min-height: 3.2rem;
    }}

    .card-descricao {{
        font-size: 0.95rem;
        line-height: 1.55;
        color: {COR_TEXTO_SUAVE};
        min-height: 6rem;
        margin-bottom: 0.7rem;
    }}

    .card-tags {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;
        min-height: 2rem;
        margin-bottom: 0.9rem;
    }}

    .tag {{
        font-size: 0.78rem;
        padding: 0.15rem 0.6rem;
        border-radius: 999px;
        color: {COR_TEXTO};
        background: rgba(220, 38, 38, 0.14);
        border: 1px solid rgba(220, 38, 38, 0.35);
    }}

    [class*="st-key-card_"] a[data-testid="stBaseLinkButton-secondary"]:hover,
    [class*="st-key-card_"] a:hover {{
        border-color: {COR_DESTAQUE};
        color: {COR_DESTAQUE};
    }}

    @media (prefers-reduced-motion: reduce) {{
        [class*="st-key-card_"] {{
            transition: none;
        }}
    }}
</style>
"""

# IMAGENS

@st.cache_data(show_spinner=False)
def _carregar_miniatura(caminho: str):
    """Abre a imagem, recorta no formato padrão e mantém em cache."""
    with Image.open(caminho) as original:
        return ImageOps.fit(
            original.convert("RGB"),
            TAMANHO_MINIATURA,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )


def exibir_imagem(caminho: Path, padronizar: bool = False) -> None:
    """Exibe uma imagem; se o arquivo não existir, mostra um aviso discreto."""
    if not caminho.exists():
        st.caption(f"Imagem não encontrada: {caminho.name}")
        return

    if padronizar:
        st.image(_carregar_miniatura(str(caminho)), use_container_width=True)
    else:
        st.image(str(caminho), use_container_width=True)

# COMPONENTES
def _cartao_projeto(indice: int, projeto: dict) -> None:
    """Desenha um cartão de projeto."""
    tags = "".join(
        f'<span class="tag">{escape(tag)}</span>'
        for tag in projeto["tecnologias"]
    )

    with st.container(key=f"card_{indice}"):
        exibir_imagem(projeto["imagem"], padronizar=True)

        st.markdown(
            f'<div class="card-titulo">{escape(projeto["titulo"])}</div>'
            f'<div class="card-descricao">{escape(projeto["descricao"])}</div>'
            f'<div class="card-tags">{tags}</div>',
            unsafe_allow_html=True,
        )

        st.link_button(
            projeto["botao"],
            projeto["link"],
            use_container_width=True,
        )


def _cabecalho_pagina() -> None:
    st.markdown(
        '<div class="pagina-titulo">Projetos acadêmicos</div>'
        '<div class="pagina-linha"></div>'
        '<div class="pagina-subtitulo">'
        "Aplicações que desenvolvi durante a graduação, de dashboards e "
        "inteligência artificial a ferramentas de redes, segurança e "
        "automação. O código está disponível no GitHub."
        "</div>",
        unsafe_allow_html=True,
    )

# PÁGINA PRINCIPAL
def exibir_projetos() -> None:
    st.markdown(CSS, unsafe_allow_html=True)

    if st.button("⬅ Voltar ao início"):
        st.session_state.pagina = "inicio"
        st.rerun()

    exibir_imagem(IMAGEM_BANNER)

    st.divider()
    _cabecalho_pagina()

    # Percorre a lista em blocos de 3 projetos por linha
    for inicio in range(0, len(PROJETOS), COLUNAS_POR_LINHA):
        bloco = PROJETOS[inicio:inicio + COLUNAS_POR_LINHA]
        colunas = st.columns(COLUNAS_POR_LINHA, gap="large")

        for deslocamento, (coluna, projeto) in enumerate(zip(colunas, bloco)):
            with coluna:
                _cartao_projeto(inicio + deslocamento, projeto)

        st.write("")

    st.divider()
    exibir_imagem(IMAGEM_ESPERAR)
    st.divider()