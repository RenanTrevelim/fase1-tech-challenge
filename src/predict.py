import joblib
import pandas as pd

COL_ENTRADA = joblib.load("models/colunas_entrada.pkl")
COL_MODELO = joblib.load("models/colunas_modelo.pkl")

preprocessamento = joblib.load("models/pre_processamento.pkl")
modelo = joblib.load("models/modelo_gradiente_boosting.pkl")

def predict(dados):
    
    df = pd.DataFrame(dados)

    df['entrega_problematica'] = ((df['delivery_delay_days'] > 0) & (df['delivery_attempts'] > 1)).astype(int)
    df['cliente_muito_acionado'] = (df['customer_service_contacts'] >= 3).astype(int)
    
    df = df[COL_ENTRADA]

    df_transformado = preprocessamento.transform(df)

    df_transformado = pd.DataFrame(df_transformado, columns=COL_MODELO)

    previsao = modelo.predict(df_transformado)

    return previsao