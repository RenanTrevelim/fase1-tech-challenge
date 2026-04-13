import joblib
import pandas as pd

COL_ENTRADA = joblib.load("models/colunas_entrada.pkl")
COL_MODELO = joblib.load("models/colunas_modelo.pkl")

preprocessamento = joblib.load("models/pre_processamento.pkl")
modelo = joblib.load("models/modelo_regressao_linear.pkl")

def predict(dados):
    
    df = pd.DataFrame(dados)
    df = df[COL_ENTRADA]

    df_transformado = preprocessamento.transform(df)

    df_transformado = pd.DataFrame(df_transformado, columns=COL_MODELO)

    previsao = modelo.predict(df_transformado)

    return previsao