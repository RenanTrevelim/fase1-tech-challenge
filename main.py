import streamlit as st
import pandas as pd
from src.predict import predict


st.set_page_config(
    page_title="Previsão de NPS",
    page_icon="📈",
    layout="wide"
)


def to_csv(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")


def classificar_nps(valor: float) -> str:
    if valor <= 6:
        return "Detrator"
    elif valor <= 8:
        return "Neutro"
    return "Promotor"


st.title("📈 Previsão de NPS")
st.write("Faça upload de um arquivo CSV para análise em lote.")

arquivo = st.file_uploader("Envie o arquivo CSV", type=["csv"])

if arquivo is not None:
    try:
        df = pd.read_csv(arquivo)

        if df.empty:
            st.warning("O arquivo enviado está vazio.")
            st.stop()

        st.subheader("Prévia do arquivo")
        st.dataframe(df.head(), use_container_width=True)

        with st.spinner("Gerando previsões..."):
            previsoes = predict(df)

        df_resultado = df.copy()
        df_resultado["nps_previsto"] = previsoes
        df_resultado["nps_previsto"] = df_resultado["nps_previsto"].clip(0, 10).round(2)
        df_resultado["classificacao_nps"] = df_resultado["nps_previsto"].apply(classificar_nps)

        total_registros = len(df_resultado)
        media_nps = df_resultado["nps_previsto"].mean()
        minimo_nps = df_resultado["nps_previsto"].min()
        maximo_nps = df_resultado["nps_previsto"].max()

        detratores = (df_resultado["classificacao_nps"] == "Detrator").sum()
        neutros = (df_resultado["classificacao_nps"] == "Neutro").sum()
        promotores = (df_resultado["classificacao_nps"] == "Promotor").sum()

        st.markdown("---")
        st.subheader("Resumo das previsões")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total de registros", total_registros)
            st.caption("Quantidade processada no arquivo")

        with col2:
            st.metric("NPS médio previsto", f"{media_nps:.2f}")
            st.caption("Média das previsões geradas")

        with col3:
            st.metric("Menor NPS previsto", f"{minimo_nps:.2f}")
            st.caption("Valor mínimo encontrado")

        with col4:
            st.metric("Maior NPS previsto", f"{maximo_nps:.2f}")
            st.caption("Valor máximo encontrado")

        st.markdown("---")
        st.subheader("Distribuição por classificação")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("## 🔴 Detratores")
            st.write(f"Quantidade: **{detratores}**")

        with c2:
            st.markdown("## 🟡 Neutros")
            st.write(f"Quantidade: **{neutros}**")

        with c3:
            st.markdown("## 🟢 Promotores")
            st.write(f"Quantidade: **{promotores}**")

        st.markdown("---")
        st.subheader("Prévia do resultado")

        colunas_preview = ["nps_previsto", "classificacao_nps"]
        if "customer_id" in df_resultado.columns:
            colunas_preview = ["customer_id"] + colunas_preview

        st.dataframe(
            df_resultado,
            use_container_width=True,
            hide_index=True,
            height=400
        )

        st.download_button(
            label="Baixar CSV com previsões",
            data=to_csv(df_resultado),
            file_name="resultado_previsao_nps.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")

else:
    st.info("Faça o upload de um arquivo CSV para começar.")