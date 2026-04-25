import streamlit as st
import pandas as pd
from src.predict import predict




st.set_page_config(
    page_title="Motor de Decisão de NPS",
    page_icon="📈",
    layout="wide"
)


def to_csv(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")


def segmentar_risco(prob_detrator: float) -> str:
    if prob_detrator <= 0.3:
        return "Seguro"
    elif prob_detrator <= 0.6:
        return "Neutro"
    elif prob_detrator <= 0.8:
        return "Atenção"
    return "Crítico"


def definir_desconto(segmento: str) -> int:
    if segmento == "Crítico":
        return 40
    elif segmento == "Atenção":
        return 20
    elif segmento == "Neutro":
        return 10
    return 0


def recomendar_acao(segmento: str) -> str:
    if segmento == "Crítico":
        return "Cupom alto + contato imediato"
    elif segmento == "Atenção":
        return "Cupom moderado + acompanhamento"
    elif segmento == "Neutro":
        return "Ação preventiva"
    return "Sem ação"


st.title("📈 Motor de Decisão de NPS")
st.write(
    "Faça upload de um arquivo CSV para estimar a probabilidade de cada cliente se tornar detrator, "
    "segmentar o risco e priorizar ações de retenção."
)

arquivo = st.file_uploader("Envie o arquivo CSV", type=["csv"])

if arquivo is not None:
    try:
        df = pd.read_csv(arquivo)
        df.columns = ['idade_cliente', 'regiao_cliente', 'tempo_cliente_meses',
       'valor_pedido', 'quantidade_itens', 'valor_desconto',
       'parcelas_pagamento', 'tempo_entrega_dias', 'atraso_entrega_dias',
       'valor_frete', 'tentativas_entrega', 'contatos_atendimento',
       'tempo_resolucao_dias', 'nps', 'numero_reclamacoes']

        if df.empty:
            st.warning("O arquivo enviado está vazio.")
            st.stop()

        st.subheader("Prévia do arquivo")
        st.dataframe(df.head(), use_container_width=True)

        with st.spinner("Gerando previsões e análises..."):
            probabilidades = predict(df)

        df_resultado = df.copy()

        df_resultado["prob_detrator"] = pd.Series(probabilidades, index=df_resultado.index).clip(0, 1).round(4)
        df_resultado["segmentacao_cliente"] = df_resultado["prob_detrator"].apply(segmentar_risco)
        df_resultado["desconto_percentual"] = df_resultado["segmentacao_cliente"].apply(definir_desconto)
        df_resultado["acao_sugerida"] = df_resultado["segmentacao_cliente"].apply(recomendar_acao)

        if "valor_pedido" in df_resultado.columns:
            df_resultado["prioridade_financeira"] = (
                df_resultado["prob_detrator"] * df_resultado["valor_pedido"]
            ).round(2)
        elif "order_value" in df_resultado.columns:
            df_resultado["prioridade_financeira"] = (
                df_resultado["prob_detrator"] * df_resultado["order_value"]
            ).round(2)

        # Estimativa de valor em risco (soma total)
        valor_em_risco = df_resultado["prioridade_financeira"].sum()

        # Suposição de taxa de recuperação (ex: 30%)
        taxa_recuperacao = 0.3
        valor_recuperavel = valor_em_risco * taxa_recuperacao

        # Custo estimado das ações (baseado nos descontos)
        df_resultado["custo_acao"] = (
            df_resultado["desconto_percentual"] / 100 * df_resultado["valor_pedido"]
        )

        custo_total = df_resultado["custo_acao"].sum()

        # ROI
        roi = (valor_recuperavel - custo_total) / custo_total if custo_total > 0 else 0

        total_registros = len(df_resultado)
        media_prob_detrator = df_resultado["prob_detrator"].mean()

        criticos = (df_resultado["segmentacao_cliente"] == "Crítico").sum()
        atencao = (df_resultado["segmentacao_cliente"] == "Atenção").sum()
        neutros_risco = (df_resultado["segmentacao_cliente"] == "Neutro").sum()
        seguros = (df_resultado["segmentacao_cliente"] == "Seguro").sum()

        percentual_criticos = criticos / total_registros if total_registros > 0 else 0

        st.markdown("---")
        st.subheader("Resumo executivo")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total de registros", total_registros)
            st.caption("Quantidade processada no arquivo")

        with col2:
            st.metric("Probabilidade média de detrator", f"{media_prob_detrator:.2%}")
            st.caption("Média do risco previsto pelo modelo")

        with col3:
            st.metric("Clientes críticos", f"{percentual_criticos:.2%}")
            st.caption("Percentual de clientes em maior risco")

        st.markdown("---")
        st.subheader("Impacto financeiro estimado")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Valor em risco", f"R$ {valor_em_risco:,.2f}")

        with col2:
            st.metric("Valor recuperável", f"R$ {valor_recuperavel:,.2f}")

        with col3:
            st.metric("ROI estimado", f"{roi:.2%}")

        st.caption(
            "Valores estimados com base em hipóteses de recuperação, custo de ação e valor financeiro em risco. "
            "ROI negativo indica que, neste cenário, o custo das ações supera o valor recuperável estimado."
        )

        st.markdown("---")
        st.subheader("Distribuição por segmento de risco")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.markdown("### 🟢 Seguro")
            st.write(f"Quantidade: **{seguros}**")

        with c2:
            st.markdown("### 🟡 Neutro")
            st.write(f"Quantidade: **{neutros_risco}**")

        with c3:
            st.markdown("### 🟠 Atenção")
            st.write(f"Quantidade: **{atencao}**")

        with c4:
            st.markdown("### 🔴 Crítico")
            st.write(f"Quantidade: **{criticos}**")

        st.markdown("---")
        st.subheader("Resultado completo")

        colunas_preview = [
            "prob_detrator",
            "segmentacao_cliente",
            "desconto_percentual",
            "acao_sugerida"
        ]

        if "prioridade_financeira" in df_resultado.columns:
            colunas_preview.append("prioridade_financeira")

        if "customer_id" in df_resultado.columns:
            colunas_preview = ["customer_id"] + colunas_preview
        elif "cliente_id" in df_resultado.columns:
            colunas_preview = ["cliente_id"] + colunas_preview

        colunas_existentes = [col for col in colunas_preview if col in df_resultado.columns]

        ordem_segmento = {
            "Crítico": 3,
            "Atenção": 2,
            "Neutro": 1,
            "Seguro": 0
        }

        df_resultado["ordem_temp"] = df_resultado["segmentacao_cliente"].map(ordem_segmento)

        df_exibicao = df_resultado.sort_values(
            by=["ordem_temp", "prob_detrator"],
            ascending=[False, False]
        ).drop(columns=["ordem_temp"])

        st.dataframe(
            df_exibicao[colunas_existentes],
            use_container_width=True,
            hide_index=True,
            height=450
        )

        st.download_button(
            label="Baixar CSV com análise completa",
            data=to_csv(df_resultado),
            file_name="resultado_analise_nps.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")

else:
    st.info("Faça o upload de um arquivo CSV para começar.")