# 📊 Análise de Satisfação do Cliente (NPS) + Motor de Decisão

Este projeto vai além da previsão de NPS, propondo um **motor de decisão orientado por dados**, capaz de antecipar risco de insatisfação e priorizar ações com impacto direto na receita.

---

## 🎯 Objetivo do Projeto

O objetivo é analisar os fatores que impactam a satisfação dos clientes (NPS) e desenvolver um modelo capaz de **prever o NPS com base em dados operacionais**.

Além disso, o projeto evolui para um **sistema de decisão**, permitindo que a empresa:

- Antecipe clientes com risco de insatisfação  
- Identifique fatores críticos da experiência  
- Priorize clientes com maior impacto financeiro  
- Direcione ações de retenção de forma estratégica  

---

## 📂 Base de Dados

Dataset com informações da jornada do cliente em um e-commerce:

###  Variáveis numéricas
- `nps_score`  
- `delivery_delay_days`  
- `customer_service_contacts`  
- `complaints_count`  
- `csat_internal_score`  
- `order_value`  
- `items_quantity`  
- `discount_value`  
- `payment_installments`  
- `delivery_time_days`  
- `customer_age`  
- `customer_tenure_months`  
- `repeat_purchase_30d`  

###  Variável categórica
- `customer_region`

###  Identificadores
- `customer_id`, `order_id`

---

## 🔍 Principais Insights (EDA)

- Alta concentração de **clientes detratores (~74%)**
- Principais drivers de insatisfação:
  -  Atraso na entrega  
  -  Número de reclamações  
  - Contatos com atendimento  
- Principal driver positivo:
  -  CSAT interno  

 Foi identificado um **ponto de ruptura (~2 dias de atraso)**, onde o NPS começa a cair drasticamente.

---

## 🧠 Modelagem Preditiva

Foram testados diversos modelos de regressão:

- Linear Regression  
- Decision Tree  
- Random Forest  
- Gradient Boosting  
- XGBoost  
- LightGBM  

###  Modelo escolhido:
**Gradient Boosting**

**Motivos:**
- Melhor desempenho (RMSE e R²)
- Maior estabilidade (cross-validation)
- Boa capacidade de generalização

---

## 🔧 Feature Engineering

Variáveis criadas com base no EDA:

- `entrega_problematica` → atraso + múltiplas tentativas  
- `cliente_muito_acionado` → alto volume de contatos  

👉 Essas features ajudam o modelo a capturar padrões de insatisfação de forma mais direta.

---

## 🔁 Validação do Modelo

Cross-validation (5 folds):

- RMSE médio: **~1.48**
- R² médio: **~0.65**
- Baixa variância → modelo **estável e confiável**

---

## 🚀 Geração de Valor (Diferencial do Projeto)

O modelo foi transformado em um **motor de decisão de negócio**.

---

###  1. Cálculo de Risco

```python
risco = (10 - nps_previsto) / 10
```

Permite transformar a previsão de NPS em uma métrica acionável:

- Quanto menor o NPS → maior o risco  
- Facilita priorização e tomada de decisão  

---

###  2. Segmentação de Clientes

- 🟢 **Seguro**  
- 🟡 **Neutro**  
- 🟠 **Atenção**  
- 🔴 **Crítico**  

👉 Permite identificar rapidamente quais clientes exigem ação imediata  

---

###  3. Estratégia de Ação

- 🔴 **Crítico** → 40% de desconto  
- 🟠 **Atenção** → 20% de desconto  
- 🟡 **Neutro** → 10% de desconto  
- 🟢 **Seguro** → sem ação  

👉 A empresa deixa de agir de forma genérica e passa a atuar de forma direcionada e eficiente  

---

###  4. Prioridade Financeira

```python
prioridade = risco × order_value
```

Essa métrica representa uma estimativa de receita em risco, permitindo:

- Identificar clientes mais críticos financeiramente  
- Priorizar ações com maior retorno  
- Otimizar o uso de incentivos  

 **Principal ganho:**

> Não basta saber quem está insatisfeito — é preciso saber quem impacta mais a receita.  

---

##  Resultado

O sistema permite:

- Antecipar churn  
- Priorizar clientes críticos  
- Reduzir desperdício de incentivos  
- Maximizar retenção  

---

## 🖥️ Aplicação (Streamlit)

Foi desenvolvida uma aplicação interativa que operacionaliza o modelo.

###  Funcionalidades:
- Upload de CSV  
- Previsão de NPS  
- Cálculo de risco  
- Segmentação automática  
- Sugestão de ações  
- Download dos resultados  

👉 Interface simples para uso direto pelo negócio  

---

## 🏁 Conclusão

O projeto evolui de uma análise de dados para um **sistema de decisão orientado por risco e valor**, permitindo:

- Melhorar a experiência do cliente  
- Reduzir churn  
- Aumentar retenção  
- Otimizar recursos  

👉 Transformando dados em ação com impacto real no negócio.

---

## 🚀 Como Reproduzir os Resultados

### 1. Clonar o repositório
```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```


### 2. Criar ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
```


### 3. Instalar dependências
```bash
pip install -r requirements.txt
```


### 4. Executar a aplicação
```bash
streamlit run main.py
```
