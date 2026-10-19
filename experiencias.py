import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from html import escape

# DADOS PROFISSIONAIS
# ATENÇÃO: os salários são ilustrativos.
# Substitua pelos valores reais antes de publicar.

experiencias = [{
        "empresa": "Warm Brasil",
        "cargo": "Agente de Atendimento Digital",
        "inicio": "2019-01-01",
        "fim": "2019-07-31",
        "salario": 1300,
        "local": "Rio de Janeiro, Brasil",
        "modalidade": "Presencial",
        "atividades": [
            "Atendimento ao cliente via chat e esclarecimento de dúvidas.",
            "Análise de solicitações e direcionamento de tratativas.",
            "Comunicação clara e foco na experiência do cliente.",
            "Organização de informações e gestão de demandas."]},

       {"empresa": "Crown Ipanema",
        "cargo": "Auxiliar de serviços gerais",
        "inicio": "2020-07-01",
        "fim": "2020-09-18",
        "salario": 1115,
        "local": "Rio de Janeiro, Brasil",
        "modalidade": "Presencial",
        "atividades": [
            "Atendimento presencial e digital aos alunos, prestando informações sobre planos, horários, modalidades e serviços oferecidos.",
            "Recepção de alunos e visitantes, proporcionando um atendimento cordial e uma experiência positiva.",
            "Serviços Gerais, limpeza, organização",
            "Esclarecimento de dúvidas, resolução de solicitações e direcionamento de demandas à equipe responsável."]},

       {"empresa": "CreditCash",
        "cargo": "Analista de Backoffice",
        "inicio": "2020-10-01",
        "fim": "2020-12-31",
        "salario": 1500,
        "local": "São Paulo, Brasil",
        "modalidade": "Presencial",
        "atividades": [
            "Atendimento ao cliente e tratativas operacionais via backoffice.",
            "Acompanhamento de demandas e comunicação com áreas internas.",
            "Organização do fluxo de demandas e resolução de solicitações."]},

       {"empresa": "CreditCash",
        "cargo": "Agente de Atendimento Digital",
        "inicio": "2020-12-01",
        "fim": "2021-10-31",
        "salario": 1750,
        "local": "São Paulo, Brasil",
        "modalidade": "Presencial",
        "atividades": [
            "Implantação do canal de atendimento via chat.",
            "Suporte direto ao cliente e acompanhamento das solicitações.",
            "Organização do fluxo de demandas e adaptação da equipe ao novo formato."]},

       {"empresa": "CreditCash",
        "cargo": "Assistente Administrativo",
        "inicio": "2021-10-01",
        "fim": "2023-02-28",
        "salario": 1900,
        "local": "São Paulo, Brasil",
        "modalidade": "Presencial",
        "atividades": [
            "Organização e controle das demandas operacionais.",
            "Separação, distribuição e acompanhamento das atividades da equipe.",
            "Suporte administrativo às equipes presenciais e home office.",
            "Participação em reuniões operacionais e alinhamentos estratégicos."]},

       {"empresa": "Intervalor",
        "cargo": "Analista Digital",
        "inicio": "2023-02-01",
        "fim": "2023-03-31",
        "salario": 1389.89,
        "local": "São Paulo, Brasil",
        "modalidade": "Híbrido",
        "atividades": [
            "Atendimento via chat do produto Vivo.",
            "Análise de solicitações e tratativas internas.",
            "Organização do fluxo de demandas e alinhamento com a equipe.",
            "Desenvolvimento de habilidades em gestão operacional e comunicação."]},

       {"empresa": "Intervalor",
        "cargo": "Assistente Administrativo",
        "inicio": "2023-03-01",
        "fim": "2023-08-31",
        "salario": 1800,
        "local": "São Paulo, Brasil",
        "modalidade": "Híbrido",
        "atividades": [
            "Organização e acompanhamento das operações.",
            "Administração das equipes presencial e home office.",
            "Controle e separação de demandas e acompanhamento de relatórios.",
            "Participação em reuniões estratégicas e suporte administrativo."]},

       {"empresa": "Verisure",
        "cargo": "Operador de Manutenção Jr.",
        "inicio": "2023-10-01",
        "fim": "2025-03-31",
        "salario": 1530.36,
        "local": "São Paulo, Brasil",
        "modalidade": "Presencial",
        "atividades": [
            "Atendimento e suporte ao cliente na área de manutenção.",
            "Acompanhamento de solicitações e comunicação com equipes técnicas.",
            "Verificação de disponibilidade de equipes e alinhamento de prazos.",
            "Registro de informações e acompanhamento das demandas.",
            "Organização de processos internos e qualidade no atendimento."]},
       
       {"empresa": "360 Suítes",
        "cargo": "Agente de Reservas Pleno",
        "inicio": "2025-02-01",
        "fim": "2026-08-31",
        "salario": 2500,
        "local": "São Paulo, Brasil",
        "modalidade": "Híbrido",
        "atividades": [
            "Gestão da jornada do hóspede, da confirmação da reserva ao encerramento da estadia.",
            "Atendimento e suporte por Airbnb, Booking.com e demais OTAs.",
            "Intermediação entre hóspedes, manutenção e governança.",
            "Resolução de ocorrências e acompanhamento de demandas.",
            "Organização operacional e gestão de múltiplas solicitações.",
            "Contribuição para a eficiência dos processos e satisfação dos hóspedes."]}]

# FUNÇÃO AUXILIAR: DURAÇÃO
def duracao_empresa(inicio, fim):
    meses = ((fim.year - inicio.year) * 12 + fim.month - inicio.month + 1)

    anos, resto = divmod(meses, 12)
    partes = []

    if anos:
        partes.append(f"{anos} ano" + ("s" if anos != 1 else ""))

    if resto:
        partes.append(f"{resto} " + ("mês" if resto == 1 else "meses"))

    return " e ".join(partes) if partes else "Menos de 1 mês"

# FUNÇÃO PRINCIPAL
# CHAMADA PELO Portfolio.py
def exibir_experiencias():

# ESTILO VISUAL
    st.markdown("""
    <style>
    .exp-titulo {
        color: #FFFFFF;
        font-size: 36px;
        font-weight: 800;
        margin-bottom: 8px;}

    .exp-linha {
        background: #B91C1C;
        width: 70px;
        height: 4px;
        border-radius: 10px;
        margin-bottom: 20px;}

    .exp-intro {
        color: #D9DDE3;
        font-size: 16px;
        line-height: 1.8;
        margin-bottom: 25px;}

    .exp-card {
        background: linear-gradient(135deg, #1C1C1C, #101010);
        border: 1px solid #383838;
        border-left: 4px solid #B91C1C;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 18px;
        transition: 0.3s ease;}

    .exp-card:hover {
        border-color: #B91C1C;
        transform: translateY(-3px);
        box-shadow: 0 10px 28px rgba(0,0,0,0.35);}

    .exp-empresa {
        font-size: 24px;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 7px;}

    .exp-periodo {
        font-size: 13px;
        color: #B8BEC9;
        margin-bottom: 16px;}

    .exp-cargo {
        font-size: 17px;
        font-weight: 700;
        color: #FFFFFF;
        margin-top: 15px;
        margin-bottom: 7px;}

    .exp-meta {
        font-size: 12px;
        color: #B8BEC9;
        margin-bottom: 12px;}

    .exp-atividade {
        color: #D9DDE3;
        font-size: 14px;
        line-height: 1.75;
        margin-bottom: 7px;}

    .exp-separador {
        border-top: 1px dashed #444444;
        margin: 20px 0;}

    .exp-etiqueta {
        display: inline-block;
        margin-top: 15px;
        padding: 6px 12px;
        border: 1px solid rgba(185,28,28,0.45);
        background: rgba(185,28,28,0.12);
        color: #FCA5A5;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;}
        
        
    .exp-etiqueta {
        display: inline-block;
        margin-top: 15px;
        padding: 6px 12px;
        border: 1px solid rgba(185,28,28,0.45);
        background: rgba(185,28,28,0.12);
        color: #FCA5A5;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;}

    /* CARDS INTERATIVOS */

    .exp-interativo {
        padding: 0;
        overflow: hidden;
        margin-bottom: 18px;}

    .exp-resumo {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 24px;
        cursor: pointer;
        list-style: none;
        min-height: 105px;}

    .exp-resumo::-webkit-details-marker {
        display: none;}

    .exp-resumo::marker {
        content: "";}

    .exp-resumo:hover {
        background: rgba(185, 28, 28, 0.08);}

    .exp-seta {
        color: #B91C1C;
        font-size: 26px;
        transition: transform 0.3s ease;}

    .exp-interativo[open] .exp-seta {
        transform: rotate(180deg);}

    .exp-conteudo {
        padding: 0 24px 24px;
        border-top: 1px solid #383838;}

    .exp-interativo[open] {
        border-color: #B91C1C;}

    </style>""", unsafe_allow_html=True)

# CABEÇALHO
    st.markdown("""
    <div class="exp-titulo">Linha do Tempo Profissional:</div>
    <div class="exp-linha"></div>
    <div class="exp-intro">
        Ao longo da minha trajetória, atuei em diferentes empresas
        e áreas, desenvolvendo habilidades em atendimento,
        organização de processos, gestão de demandas e suporte
        operacional, sempre com foco em eficiência, qualidade
        e melhoria da experiência do cliente.
    </div>""", unsafe_allow_html=True)

# PREPARAÇÃO DOS DADOS
    df_exp = pd.DataFrame(experiencias)

    df_exp["inicio"] = pd.to_datetime(df_exp["inicio"])
    df_exp["fim"] = pd.to_datetime(df_exp["fim"])

    df_exp = df_exp.sort_values("inicio").reset_index(drop=True)

# GRÁFICO DE EVOLUÇÃO SALARIAL
    fig = go.Figure()

    fig.add_trace(go.Scatter(
            x=df_exp["inicio"],
            y=df_exp["salario"],
            mode="lines+markers",

            line=dict(color="#B91C1C", width=4),

            marker=dict(
                size=13,
                color="#FFFFFF",
                line=dict(color="#B91C1C",width=3)),

            customdata=df_exp[["empresa", "cargo"]].to_numpy(),

            hovertemplate=("<b>%{customdata[0]}</b><br>" "%{customdata[1]}<br>" "Início: %{x|%m/%Y}<br>" "Salário: R$ %{y:,.2f}" "<extra></extra>")))

    fig.update_layout(
        height=450,
        paper_bgcolor="#0D0D0D",
        plot_bgcolor="#0D0D0D",
        font=dict(color="#D9DDE3"),
        margin=dict(l=20, r=20, t=35, b=30),
        showlegend=False,

        xaxis=dict(
            title="Linha do tempo",
            tickformat="%Y",
            gridcolor="#303030",
            showgrid=True),

        yaxis=dict(
            title="Evolução salarial (R$)",
            tickprefix="R$ ",
            gridcolor="#303030",
            showgrid=True,
            rangemode="tozero"),

        hoverlabel=dict(
            bgcolor="#222222",
            font_color="#FFFFFF",
            bordercolor="#B91C1C"))

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    st.caption(
        "Passe o mouse sobre os pontos para visualizar "
        "a empresa, o cargo e o salário. "
        "Os salários cadastrados inicialmente são ilustrativos.")

# MINHA TRAJETÓRIA
    st.markdown("""
    <div style="font-size:27px;font-weight:800;color:#FFFFFF;
                margin-top:30px;margin-bottom:10px;">Histórico Profissional:
    </div>
    <div style="width:60px;height:3px;background:#B91C1C;
                margin-bottom:25px;border-radius:10px;"></div>
    """, unsafe_allow_html=True)

    ordem_empresas = [
            "Warm Brasil",
            "Crown Ipanema",
            "CreditCash",
            "Intervalor",
            "Verisure",
            "360 Suítes"]

# CARDS DAS EMPRESAS
    colunas = st.columns(2, gap="medium")

    for indice, empresa in enumerate(ordem_empresas):

        coluna_atual = colunas[indice % 2]

        registros = df_exp[df_exp["empresa"] == empresa].sort_values("inicio", ascending=False)

        if registros.empty:
            continue

        inicio = registros["inicio"].min()
        fim = registros["fim"].max()

        periodo = (f'{inicio.strftime("%m/%Y")} — ' f'{fim.strftime("%m/%Y")}')

        tempo = duracao_empresa(inicio, fim)

        cargos_html = ""

        for _, item in registros.iterrows():

            atividades_html = "".join(
                f'<div class="exp-atividade">'
                f'• {escape(str(atividade))}'
                f'</div>'
                for atividade in item["atividades"])

            if cargos_html:
                cargos_html += (
                    '<div class="exp-separador"></div>')

            cargos_html += (
                f'<div class="exp-cargo">'
                f'↗ {escape(str(item["cargo"]))}'
                f'</div>'

                f'<div class="exp-meta">'
                f'📅 {item["inicio"].strftime("%m/%Y")} — '
                f'{item["fim"].strftime("%m/%Y")}'
                f' &nbsp; | &nbsp; '
                f'📍 {escape(str(item["local"]))}'
                f' &nbsp; | &nbsp; '
                f'{escape(str(item["modalidade"]))}'
                f'</div>'

                f'{atividades_html}')

# HTML sem indentação para evitar
# que o Streamlit mostre código na tela.
        html_card = (
            '<details class="exp-card exp-interativo">'

            '<summary class="exp-resumo">'

            '<div>'
            f'<div class="exp-empresa">'
            f'{escape(str(empresa))}'
            f'</div>'

            f'<div class="exp-periodo">'
            f'{periodo} &nbsp; • &nbsp; {tempo}'
            f'</div>'
            '</div>'

            '<span class="exp-seta">⌄</span>'

            '</summary>'

            '<div class="exp-conteudo">'
            f'{cargos_html}'
            '</div>'

            '</details>')

        # EXIBIÇÃO DOS CARDS NAS DUAS COLUNAS
        with coluna_atual:
            st.markdown(html_card, unsafe_allow_html=True)
