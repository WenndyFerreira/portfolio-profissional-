import base64
import re
from html import escape
from io import BytesIO
from pathlib import Path

import numpy as np
import streamlit as st
from PIL import Image

# CONFIGURAÇÃO
PASTA_PROJETO = Path(__file__).resolve().parent
IMAGEM_BOTAO = PASTA_PROJETO / "BotaoCertificado.png"

# True: mostra os certificados mais recentes primeiro (usa o campo "emissao").
# False: mantém a ordem exata da lista abaixo.
ORDENAR_POR_DATA = True
COR_DESTAQUE = "#DC2626"
COR_TEXTO = "#F4F4F5"
COR_TEXTO_SUAVE = "#A1A1AA"
COR_BORDA = "rgba(255, 255, 255, 0.10)"
COR_BORDA_HOVER = "rgba(220, 38, 38, 0.60)"
COR_FUNDO_CARD = "rgba(255, 255, 255, 0.03)"
PERFIL_LINKEDIN = "https://www.linkedin.com/in/wenndy-ferreira-875a32251/"
_SUFIXO = "/treasury/?profileId=ACoAAD5ETVkBFr7TlzPb9cxU3x1tHE8kRnWQvvc"

def _link_certificado(codigo: str) -> str:
    return f"{PERFIL_LINKEDIN}overlay/Certifications/{codigo}{_SUFIXO}"

# Para adicionar um certificado, inclua um novo dicionário nesta lista.
CERTIFICADOS = [
       {"titulo": "Power BI Avançado",
        "instituicao": "Expert Cursos",
        "emissao": "Outubro de 2026",
        "carga_horaria": "30 horas",
        "link": _link_certificado("309551067"),},

       {"titulo": "Intensivão de Power BI",
        "instituicao": "Hashtag Treinamentos",
        "emissao": "Outubro de 2026",
        "carga_horaria": "8 horas",
        "link": _link_certificado("308618848"),},

       {"titulo": "Python Fundamental 1",
        "instituicao": "IFSC | Aprenda Mais",
        "emissao": "Setembro de 2026",
        "carga_horaria": "20 horas",
        "link": _link_certificado("2016697874"),},

       {"titulo": "Jornada Python",
        "instituicao": "Hashtag Treinamentos",
        "emissao": "Outubro de 2026",
        "carga_horaria": "8 horas",
        "link": _link_certificado("1443791811"),},

       {"titulo": "Redes de Computadores",
        "instituicao": "IFRS",
        "emissao": "Setembro de 2026",
        "carga_horaria": "30 horas",
        "link": _link_certificado("60288213"),},

       {"titulo": "Excel Avançado",
        "instituicao": "Expert Cursos",
        "emissao": "Fevereiro de 2023",
        "carga_horaria": "30 horas",
        "link": _link_certificado("831595137"),},

       {"titulo": "Python Fundamental 2",
        "instituicao": "IFRS",
        "emissao": "Outubro de 2026",
        "carga_horaria": "30 horas",
         "link": _link_certificado("1604438626"),},]

MESES = {
    "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4,
    "maio": 5, "junho": 6, "julho": 7, "agosto": 8,
    "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12,}

# Ícone usado quando a imagem BotaoCertificado.png não existe
ICONE_PADRAO = (
    '<svg viewBox="0 0 64 64" role="img" aria-hidden="true">'
    f'<circle cx="32" cy="32" r="30" fill="none" stroke="{COR_DESTAQUE}" '
    'stroke-width="3"/>'
    f'<path d="M20 33l8 8 16-17" fill="none" stroke="{COR_DESTAQUE}" '
    'stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
    "</svg>")

# ESTILO
CSS = f"""
<style>
    .cert-titulo {{
        font-size: 2.2rem;
        font-weight: 750;
        line-height: 1.15;
        color: {COR_TEXTO};
        margin: 0 0 0.4rem 0;}}

    .cert-linha {{
        width: 64px;
        height: 4px;
        background: {COR_DESTAQUE};
        border-radius: 999px;
        margin-bottom: 0.9rem;}}

    .cert-descricao {{
        max-width: 62ch;
        color: {COR_TEXTO_SUAVE};
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 0.6rem;}}

    .cert-resumo {{
        color: {COR_TEXTO};
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 1.6rem;}}

    .cert-grade {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 18px;
        margin-bottom: 2rem;}}

    .cert-card {{
        display: flex;
        flex-direction: column;
        gap: 14px;
        padding: 20px;
        background: {COR_FUNDO_CARD};
        border: 1px solid {COR_BORDA};
        border-radius: 14px;
        transition: border-color 0.2s ease;}}

    .cert-card:hover {{
        border-color: {COR_BORDA_HOVER};}}

    .cert-topo {{
        display: flex;
        align-items: center;
        gap: 14px;}}

    .cert-icone {{
        flex: 0 0 56px;
        width: 56px;
        height: 56px;}}

    .cert-icone img,
    .cert-icone svg {{
        width: 100%;
        height: 100%;
        display: block;
        object-fit: contain;
        border-radius: 50%;}}

    .cert-nome {{
        color: {COR_TEXTO};
        font-size: 1.05rem;
        font-weight: 700;
        line-height: 1.3;
        margin: 0;}}

    .cert-instituicao {{
        color: {COR_TEXTO_SUAVE};
        font-size: 0.88rem;
        line-height: 1.4;
        margin-top: 2px;}}

    .cert-meta {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;}}

    .cert-tag {{
        font-size: 0.78rem;
        padding: 0.15rem 0.6rem;
        border-radius: 999px;
        color: {COR_TEXTO};
        background: rgba(220, 38, 38, 0.14);
        border: 1px solid rgba(220, 38, 38, 0.35);}}

    .cert-acao {{
        margin-top: auto;
        display: block;
        text-align: center;
        padding: 0.55rem 1rem;
        border-radius: 8px;
        border: 1px solid {COR_BORDA};
        color: {COR_TEXTO} !important;
        font-size: 0.92rem;
        font-weight: 600;
        text-decoration: none !important;
        transition: border-color 0.2s ease, color 0.2s ease;}}

    a.cert-acao:hover {{
        border-color: {COR_DESTAQUE};
        color: {COR_DESTAQUE} !important;}}

    a.cert-acao:focus-visible {{
        outline: 2px solid {COR_DESTAQUE};
        outline-offset: 3px;}}

    .cert-acao-inativa {{
        color: {COR_TEXTO_SUAVE} !important;
        cursor: default;
        opacity: 0.7;}}

    @media (max-width: 550px) {{
        .cert-titulo {{ font-size: 1.8rem; }}
        .cert-grade {{ grid-template-columns: 1fr; }}}}

    @media (prefers-reduced-motion: reduce) {{
        .cert-card, .cert-acao {{ transition: none; }}}}
</style>"""

# ---------------------------------------------------------------------------
# IMAGEM DO BOTÃO
@st.cache_data(show_spinner=False)
def preparar_imagem_botao(caminho: str, modificacao: int) -> str:

    with Image.open(caminho) as original:
        imagem = original.convert("RGBA")

    dados = np.asarray(imagem).astype(np.int16)
    r, g, b, a = dados[..., 0], dados[..., 1], dados[..., 2], dados[..., 3]

    mascara = (a > 100) & (r > 140) & (r > g * 1.6) & (r > b * 1.5)
    ys, xs = np.nonzero(mascara)

    altura, largura = dados.shape[:2]

    if xs.size:
        esquerda, direita = xs.min(), xs.max()
        topo, baixo = ys.min(), ys.max()
        centro_x = int((esquerda + direita) // 2)
        centro_y = int((topo + baixo) // 2)
        tamanho = int(max(direita - esquerda, baixo - topo) * 1.12)
    else:
        centro_x, centro_y = largura // 2, altura // 2
        tamanho = min(largura, altura) // 2

    metade = max(tamanho // 2, 1)
    imagem = imagem.crop((centro_x - metade, centro_y - metade, centro_x + metade, centro_y + metade,)).resize((240, 240), Image.Resampling.LANCZOS)

    pixels = np.array(imagem)
    yy, xx = np.ogrid[:240, :240]
    fora = (xx - 120) ** 2 + (yy - 120) ** 2 > 116 ** 2
    pixels[fora, 3] = 0

    buffer = BytesIO()
    Image.fromarray(pixels, "RGBA").save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

def _icone_html(titulo: str) -> str:
    if not IMAGEM_BOTAO.exists():
        return ICONE_PADRAO

    imagem_base64 = preparar_imagem_botao(str(IMAGEM_BOTAO), IMAGEM_BOTAO.stat().st_mtime_ns)
    return (f'<img src="data:image/png;base64,{imagem_base64}" 'f'alt="Ícone do certificado {titulo}">')

# DADOS
def _chave_data(certificado: dict) -> tuple:
    texto = certificado.get("emissao", "").lower()
    ano = re.search(r"\d{4}", texto)
    mes = next((n for nome, n in MESES.items() if nome in texto), 0)
    return (int(ano.group()) if ano else 0, mes)


def _horas(certificado: dict) -> int:
    numero = re.search(r"\d+", certificado.get("carga_horaria", ""))
    return int(numero.group()) if numero else 0


def _certificados_ordenados() -> list:
    if ORDENAR_POR_DATA:
        return sorted(CERTIFICADOS, key=_chave_data, reverse=True)
    return list(CERTIFICADOS)

# COMPONENTES
def _cartao_html(certificado: dict) -> str:
    titulo = escape(certificado["titulo"])
    instituicao = escape(certificado["instituicao"])
    emissao = escape(certificado.get("emissao", ""))
    carga = escape(certificado.get("carga_horaria", ""))
    link = certificado.get("link", "").strip()

    tags = "".join(f'<span class="cert-tag">{texto}</span>' for texto in (emissao, carga) if texto)

    if link.startswith(("https://", "http://")):
        acao = (f'<a class="cert-acao" href="{escape(link, quote=True)}" ''target="_blank" rel="noopener noreferrer" 'f'aria-label="Ver certificado de {titulo}">' "Ver certificado</a>")
    else:
        acao = ('<span class="cert-acao cert-acao-inativa" ''title="Link do certificado ainda não cadastrado">' "Link indisponível</span>")

    return (
        '<div class="cert-card">'
        '<div class="cert-topo">'
        f'<div class="cert-icone">{_icone_html(titulo)}</div>'
        "<div>"
        f'<div class="cert-nome">{titulo}</div>'
        f'<div class="cert-instituicao">{instituicao}</div>'
        "</div>"
        "</div>"
        f'<div class="cert-meta">{tags}</div>'
        f"{acao}"
        "</div>")


def _cabecalho(total: int, horas: int) -> str:
    resumo = f"{total} certificados, {horas} horas de estudo"
    return (
        '<div class="cert-titulo">Certificações e formação complementar</div>'
        '<div class="cert-linha"></div>'
        '<div class="cert-descricao">'
        "Cursos e certificações que complementam minha formação "
        "acadêmica e meu desenvolvimento profissional."
        "</div>"
        f'<div class="cert-resumo">{resumo}</div>')

# PÁGINA PRINCIPAL
def exibir_certificados() -> None:
    st.markdown(CSS, unsafe_allow_html=True)

    certificados = _certificados_ordenados()
    horas_totais = sum(_horas(c) for c in certificados)

    st.markdown(_cabecalho(len(certificados), horas_totais), unsafe_allow_html=True,)

    cartoes = "".join(_cartao_html(c) for c in certificados)
    st.markdown(f'<div class="cert-grade">{cartoes}</div>', unsafe_allow_html=True,)