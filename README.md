# 📊 Análise de Satisfação do Cliente (NPS) + Motor de Decisão

💡 Este projeto vai além da previsão de NPS, propondo um sistema de decisão que permite antecipar perdas de receita e atuar de forma estratégica na retenção de clientes.

---

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo analisar os fatores que impactam a satisfação dos clientes, medida pelo **Net Promoter Score (NPS)**, e desenvolver um **modelo preditivo** capaz de estimar o NPS com base em dados operacionais.

Além disso, o projeto evolui para um **motor de decisão**, transformando previsões em ações práticas com impacto direto no negócio.

A proposta é permitir que a empresa:

- Identifique os principais fatores que influenciam a satisfação e a insatisfação dos clientes  
- Antecipe clientes com risco de se tornarem detratores  
- Priorize clientes com maior impacto financeiro  
- Direcione ações de retenção de forma estratégica  
- Reduza churn e maximize o retorno das ações  

---

## 📂 Descrição da Base de Dados

A base de dados contém informações relacionadas à jornada do cliente em um contexto de e-commerce, incluindo:

### 🔢 Variáveis numéricas
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

### 🌍 Variável categórica
- `customer_region`

### 🆔 Identificadores
- `customer_id`
- `order_id`

Essas variáveis permitem analisar tanto aspectos operacionais (logística e atendimento) quanto comportamento do cliente.

---

## 🧠 Metodologia Utilizada

O projeto foi estruturado em três etapas principais:

---

### 🔍 1. Análise Exploratória de Dados (EDA)

- Tratamento de dados nulos e duplicados  
- Estatística descritiva  
- Análise da distribuição do NPS  
- Correlação entre variáveis  
- Visualizações (boxplot, histogramas, heatmap, pairplot)  

#### 📌 Principais insights:

- Predominância de clientes com **NPS baixo (detratores)**  
- Fatores com maior impacto negativo:
  - 🔻 Atraso na entrega  
  - 🔻 Número de reclamações  
  - 🔻 Contatos com atendimento  
- Fator com maior impacto positivo:
  - 🔺 CSAT interno  
- Identificação de um **ponto crítico no CSAT (~6)**  

---

### ⚙️ 2. Modelagem Preditiva

- Modelo de regressão linear  
- Pipeline com:
  - StandardScaler  
  - OneHotEncoder  
- Divisão treino/teste com estratificação  

#### 📊 Avaliação:
- R²  
- MAE  
- RMSE  

#### 📌 Resultado:

O modelo apresenta boa capacidade de estimar o NPS com base em variáveis operacionais, permitindo antecipar a satisfação do cliente.

---

## 🚀 Geração de Valor para o Negócio

O grande diferencial deste projeto está na transformação do modelo em um **sistema de decisão orientado por dados**.

---

### ⚠️ 1. Cálculo do Risco de Insatisfação

```python
risco = (10 - nps_previsto) / 10
```

Permite transformar a previsão de NPS em uma métrica acionável:

- Quanto menor o NPS → maior o risco  
- Facilita priorização e tomada de decisão  

---

### 🧩 2. Segmentação de Clientes

- 🟢 **Seguro**  
- 🟡 **Neutro**  
- 🟠 **Atenção**  
- 🔴 **Crítico**  

👉 Permite identificar rapidamente quais clientes exigem ação imediata  

---

### 🎁 3. Estratégia de Ação

- 🔴 **Crítico** → 40% de desconto  
- 🟠 **Atenção** → 20% de desconto  
- 🟡 **Neutro** → 10% de desconto  
- 🟢 **Seguro** → sem ação  

👉 A empresa deixa de agir de forma genérica e passa a atuar de forma direcionada e eficiente  

---

### 💸 4. Prioridade Financeira

```python
prioridade = risco × order_value
```

Essa métrica representa uma estimativa de receita em risco, permitindo:

- Identificar clientes mais críticos financeiramente  
- Priorizar ações com maior retorno  
- Otimizar o uso de incentivos  

💡 **Principal ganho:**

> Não basta saber quem está insatisfeito — é preciso saber quem impacta mais a receita.  

---

### 🎯 5. Ações Recomendadas

Para cada cliente, o sistema sugere automaticamente:

- Nível de risco  
- Desconto recomendado  
- Ação de retenção  

👉 Transformando o modelo em uma ferramenta prática para operação.

---

## 🖥️ Aplicação Interativa (Streamlit)

Foi desenvolvida uma aplicação em Streamlit que permite simular o uso do modelo no dia a dia do negócio.

Funcionalidades:

- Upload de dados em CSV  
- Previsão do NPS em tempo real  
- Cálculo do risco de insatisfação  
- Segmentação automática dos clientes  
- Definição de ações de retenção  
- Download dos resultados  

📌 O modelo deixa de ser apenas analítico e passa a ser uma ferramenta prática para tomada de decisão.

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
