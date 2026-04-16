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


def segmentar_risco(risco: float) -> str:
    if risco <= 0.4:
        return "Seguro"
    elif risco <= 0.6:
        return "Neutro"
    elif risco <= 0.8:
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
    "Faça upload de um arquivo CSV para prever o NPS, identificar risco de insatisfação "
    "e priorizar clientes para ações de retenção."
)

arquivo = st.file_uploader("Envie o arquivo CSV", type=["csv"])

if arquivo is not None:
    try:
        df = pd.read_csv(arquivo)

        if df.empty:
            st.warning("O arquivo enviado está vazio.")
            st.stop()

        st.subheader("Prévia do arquivo")
        st.dataframe(df.head(), use_container_width=True)

        with st.spinner("Gerando previsões e análises..."):
            previsoes = predict(df)

        df_resultado = df.copy()

        df_resultado["nps_previsto"] = previsoes
        df_resultado["nps_previsto"] = df_resultado["nps_previsto"].clip(0, 10).round(2)

        df_resultado["risco"] = ((10 - df_resultado["nps_previsto"]) / 10).round(4)
        df_resultado["segmentacao_cliente"] = df_resultado["risco"].apply(segmentar_risco)
        df_resultado["desconto_percentual"] = df_resultado["segmentacao_cliente"].apply(definir_desconto)

        if "order_value" in df_resultado.columns:
            df_resultado["prioridade_financeira"] = (
                df_resultado["risco"] * df_resultado["order_value"]
            ).round(2)

        df_resultado["acao_sugerida"] = df_resultado["segmentacao_cliente"].apply(recomendar_acao)

        total_registros = len(df_resultado)
        media_nps = df_resultado["nps_previsto"].mean()
        media_risco = df_resultado["risco"].mean()

        criticos = (df_resultado["segmentacao_cliente"] == "Crítico").sum()
        atencao = (df_resultado["segmentacao_cliente"] == "Atenção").sum()
        neutros_risco = (df_resultado["segmentacao_cliente"] == "Neutro").sum()
        seguros = (df_resultado["segmentacao_cliente"] == "Seguro").sum()

        st.markdown("---")
        st.subheader("Resumo executivo")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total de registros", total_registros)
            st.caption("Quantidade processada no arquivo")

        with col2:
            st.metric("NPS médio previsto", f"{media_nps:.2f}")
            st.caption("Média das previsões geradas")

        with col3:
            st.metric("Risco médio", f"{media_risco:.2%}")
            st.caption("Média do risco de insatisfação")

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
            "nps_previsto",
            "risco",
            "segmentacao_cliente",
            "desconto_percentual",
            "acao_sugerida"
        ]

        if "prioridade_financeira" in df_resultado.columns:
            colunas_preview.append("prioridade_financeira")

        if "customer_id" in df_resultado.columns:
            colunas_preview = ["customer_id"] + colunas_preview

        colunas_existentes = [col for col in colunas_preview if col in df_resultado.columns]

        st.dataframe(
            df_resultado[colunas_existentes],
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