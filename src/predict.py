import joblib
import pandas as pd

COL_ENTRADA = joblib.load("models/colunas_entrada.pkl")
COL_MODELO = joblib.load("models/colunas_modelo.pkl")

preprocessamento = joblib.load("models/pre_processamento.pkl")
modelo = joblib.load("models/modelo_gradiente_boosting.pkl")

def predict(dados):
    
    df = pd.DataFrame(dados)

    df['atraso_critico'] = (df['atraso_entrega_dias'] >= 2).astype(int)

    df['problema_complexo'] = ((df['contatos_atendimento'] >= 2) & (df['tempo_resolucao_dias'] >= 3)).astype(int)

    df['reclamacao_recorrente'] = (df['numero_reclamacoes'] >= 3).astype(int)
    
    df = df[COL_ENTRADA]

    df_transformado = preprocessamento.transform(df)

    df_transformado = pd.DataFrame(df_transformado, columns=COL_MODELO)

    previsao_proba = modelo.predict_proba(df_transformado)[:, 1]

    return previsao_proba