import streamlit as st
from pathlib import Path
from PIL import Image
from html import escape
from io import BytesIO
import base64

# CONFIGURAÇÕES
PASTA_PROJETO = Path(__file__).resolve().parent

IMAGEM_BOTAO = PASTA_PROJETO / "BotaoCertificado.png"

# LISTA DE CERTIFICADOS
certificados = [
    {
        "titulo": "Power BI Avançado",
        "instituicao": "Expert Cursos",
        "emissao": "Outubro de 2026",
        "carga_horaria": "30 horas",
        "link": "https://www.linkedin.com/in/wenndy-ferreira-875a32251/overlay/Certifications/309551067/treasury/?profileId=ACoAAD5ETVkBFr7TlzPb9cxU3x1tHE8kRnWQvvc"},
    
    {
        "titulo": "Intensivão de Power BI",
        "instituicao": "Hashtag Treinamentos",
        "emissao": "Outubro de 2026",
        "carga_horaria": "8 horas",
        "link": "https://www.linkedin.com/in/wenndy-ferreira-875a32251/overlay/Certifications/308618848/treasury/?profileId=ACoAAD5ETVkBFr7TlzPb9cxU3x1tHE8kRnWQvvc"},
    
    {
        "titulo": "Python Fundamental 1",
        "instituicao": "IFSC | Aprenda Mais",
        "emissao": "Setembro de 2026",
        "carga_horaria": "20 horas",
        "link": "https://www.linkedin.com/in/wenndy-ferreira-875a32251/overlay/Certifications/2016697874/treasury/?profileId=ACoAAD5ETVkBFr7TlzPb9cxU3x1tHE8kRnWQvvc"},
    
    {
        "titulo": "Redes de Computadores",
        "instituicao": "IFRS",
        "emissao": "Setembro de 2026",
        "carga_horaria": "30 horas",
        "link": "https://www.linkedin.com/in/wenndy-ferreira-875a32251/overlay/Certifications/60288213/treasury/?profileId=ACoAAD5ETVkBFr7TlzPb9cxU3x1tHE8kRnWQvvc"},

    {
        "titulo": "Excel Avançado",
        "instituicao": "Expert Cursos",
        "emissao": "Fevereiro de 2023",
        "carga_horaria": "30 horas",
        "link": "https://www.linkedin.com/in/wenndy-ferreira-875a32251/overlay/Certifications/831595137/treasury/?profileId=ACoAAD5ETVkBFr7TlzPb9cxU3x1tHE8kRnWQvvc"}]

# RECORTAR IMAGEM DO BOTÃO
@st.cache_data
def preparar_imagem_botao(caminho, modificacao):

    with Image.open(caminho) as original:
        imagem = original.convert("RGBA")

    largura, altura = imagem.size

# Localizar a borda vermelha do botão
    pixels = imagem.load()
    pontos = []

    for y in range(altura):
        for x in range(largura):

            r, g, b, a = pixels[x, y]

            if (a > 100 and r > 140 and r > g * 1.6 and r > b * 1.5):
                pontos.append((x, y))

    if pontos:

        esquerda = min(p[0] for p in pontos)
        direita = max(p[0] for p in pontos)
        topo = min(p[1] for p in pontos)
        baixo = max(p[1] for p in pontos)

        centro_x = (esquerda + direita) // 2
        centro_y = (topo + baixo) // 2

        tamanho = max(direita - esquerda, baixo - topo)

# Pequena margem para preservar a borda
        tamanho = int(tamanho * 1.12)

    else:

        # Recorte central caso não encontre a borda
        centro_x = largura // 2
        centro_y = altura // 2
        tamanho = min(largura, altura) // 2

    metade = tamanho // 2

    imagem = imagem.crop((
        centro_x - metade,
        centro_y - metade,
        centro_x + metade,
        centro_y + metade))

    imagem = imagem.resize((240, 240), Image.Resampling.LANCZOS)

# Remover o fundo externo ao círculo
    pixels = imagem.load()
    centro = 120
    raio = 116

    for y in range(240):
        for x in range(240):

            distancia = ((x - centro) ** 2 + (y - centro) ** 2) ** 0.5

            if distancia > raio:
                r, g, b, _ = pixels[x, y]
                pixels[x, y] = (r, g, b, 0)

    buffer = BytesIO()
    imagem.save(buffer, format="PNG")

    return base64.b64encode(buffer.getvalue()).decode("utf-8")

# FUNÇÃO PRINCIPAL
def exibir_certificados():

    # ESTILO VISUAL
    st.markdown("""
    <style>

    .cert-titulo {
        font-size: 34px;
        font-weight: 750;
        color: #FFFFFF;
        margin-bottom: 10px;}

    .cert-linha {
        width: 65px;
        height: 4px;
        background: #DC2626;
        border-radius: 10px;
        margin-bottom: 20px;}

    .cert-descricao {
        font-size: 16px;
        line-height: 1.8;
        color: #BDBDBD;
        margin-bottom: 30px;}

    /* ORGANIZAÇÃO DOS CERTIFICADOS */

    .cert-grade {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        gap: 24px;
        margin-top: 20px;
        margin-bottom: 30px;}

    .cert-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        text-align: center;
        gap: 12px;
        min-width: 0;}

    /* BOTÃO REDONDO */

    .cert-botao {
        width: 100px;
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        text-decoration: none;
        transition: transform 0.25s ease;}

    .cert-botao img {
        width: 100%;
        height: 100%;
        object-fit: contain;
        border-radius: 50%;
        display: block;}

    .cert-botao:hover {
        transform: scale(1.08);}

    .cert-botao:focus-visible {
        outline: 2px solid #DC2626;
        outline-offset: 5px;}

    .cert-botao-inativo {
        cursor: default;
        opacity: 0.65;}

    .cert-botao-inativo:hover {
        transform: none;}

    /* NOME CENTRALIZADO */

    .cert-nome {
        color: #FFFFFF;
        font-size: 14px;
        font-weight: 600;
        line-height: 1.5;
        text-align: center;
        width: 100%;
        margin: 0;}

    .cert-instituicao {
        color: #A0A0A0;
        font-size: 12px;
        text-align: center;
        line-height: 1.4;}

    /* RESPONSIVIDADE */

    @media (max-width: 900px) {
        .cert-grade {
            grid-template-columns: repeat(3, minmax(0, 1fr));}
    }

    @media (max-width: 550px) {
        .cert-grade {
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 25px 12px;}

        .cert-botao {
            width: 85px;
            height: 85px;}

        .cert-nome {
            font-size: 12px;}
    }

    </style>""", unsafe_allow_html=True)

# TÍTULO

    st.markdown("""
    <div class="cert-titulo">
        Certificações e Formação Complementar
    </div>

    <div class="cert-linha"></div>

    <div class="cert-descricao">
        Cursos e certificações que complementam minha
        formação acadêmica e meu desenvolvimento profissional.
    </div>""", unsafe_allow_html=True)

# CARREGAR IMAGEM
    if not IMAGEM_BOTAO.exists():
        st.warning("Imagem BotaoCertificado.png não encontrada.")
        return

    imagem_base64 = preparar_imagem_botao(
        str(IMAGEM_BOTAO),
        IMAGEM_BOTAO.stat().st_mtime_ns)

# BOTÕES COM LINKS EXTERNOS
    cards_html = []

    for certificado in certificados:

        titulo = escape(certificado["titulo"])
        instituicao = escape(certificado["instituicao"])

        link = certificado.get("link", "").strip()

        imagem_html = (
            f'<img src="data:image/png;base64,{imagem_base64}" '
            f'alt="Acessar certificado de {titulo}">')

        if link.startswith(("https://", "http://")):

            botao_html = (
                f'<a class="cert-botao" '
                f'href="{escape(link, quote=True)}" '
                f'target="_blank" '
                f'rel="noopener noreferrer" '
                f'aria-label="Visualizar certificado de {titulo}">'
                f'{imagem_html}'
                '</a>')

        else:

            botao_html = (
                '<div class="cert-botao cert-botao-inativo" '
                'title="Link do certificado ainda não cadastrado">'
                f'{imagem_html}'
                '</div>')

        cards_html.append(
            '<div class="cert-item">'
            f'{botao_html}'
            f'<div class="cert-nome">{titulo}</div>'
            f'<div class="cert-instituicao">{instituicao}</div>'
            '</div>')

    st.markdown(
        '<div class="cert-grade">'
        + "".join(cards_html)
        + '</div>',
        unsafe_allow_html=True)
