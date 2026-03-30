# 📊 Análise de Satisfação do Cliente (NPS) + Modelo Preditivo

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo analisar os fatores que impactam a satisfação dos clientes, medida pelo **Net Promoter Score (NPS)**, e desenvolver um **modelo preditivo** capaz de estimar o NPS com base em dados operacionais.

A proposta é permitir que a empresa:
- Identifique os principais fatores que influenciam a satisfação e a insatisfação dos clientes
- Antecipe clientes com risco de se tornarem detratores
- Apoie decisões estratégicas para melhoria da experiência do cliente

---

## 📂 Descrição da Base de Dados

A base de dados contém informações relacionadas à jornada do cliente em um contexto de e-commerce, incluindo:

### 🔢 Variáveis numéricas
- `nps_score`: nota de satisfação do cliente (0 a 10)
- `delivery_delay_days`: atraso na entrega
- `customer_service_contacts`: número de contatos com atendimento
- `complaints_count`: número de reclamações
- `csat_internal_score`: score interno de satisfação
- `order_value`: valor do pedido
- `items_quantity`: quantidade de itens
- `discount_value`: valor de desconto
- `payment_installments`: número de parcelas
- `delivery_time_days`: tempo de entrega
- `customer_age`: idade do cliente
- `customer_tenure_months`: tempo como cliente
- `repeat_purchase_30d`: indicador de recompra

### 🌍 Variável categórica
- `customer_region`: região do cliente

### 🆔 Identificadores
- `customer_id`
- `order_id`

---

## 🧠 Metodologia Utilizada

O projeto foi dividido em duas etapas principais:

---

### 🔍 1. Análise Exploratória de Dados (EDA)

Foram realizadas análises estatísticas e visuais para entender o comportamento dos dados:

- Verificação de dados nulos e duplicados
- Estatística descritiva
- Análise da distribuição do NPS
- Identificação de correlações entre variáveis
- Visualizações (boxplot, histogramas, heatmap, pairplot)

#### 📌 Principais insights:
- A maioria dos clientes apresenta **NPS baixo (tendência a detratores)**
- Fatores com maior impacto negativo:
  - Atraso na entrega
  - Número de reclamações
  - Contatos com atendimento
- Fator com maior impacto positivo:
  - CSAT interno
- Identificação de um possível **ponto de ruptura** no CSAT (~6)

---

### ⚙️ 2. Modelagem Preditiva

#### 🎯 Abordagem escolhida: Regressão

O NPS foi tratado como uma variável contínua (0 a 10), permitindo maior precisão na previsão.

#### 🔄 Etapas realizadas:

1. **Criação de categorias de NPS** (para estratificação)
2. **Divisão treino/teste com estratificação**
3. **Pré-processamento com pipeline:**
   - StandardScaler (variáveis numéricas)
   - OneHotEncoder (variáveis categóricas)
4. **Modelagem:**
   - Regressão Linear (Scikit-learn)
   - Regressão com StatsModels (interpretação dos coeficientes)

#### 📊 Avaliação do modelo:
- R² (coeficiente de determinação)
- MAE (erro absoluto médio)
- RMSE (erro quadrático médio)

#### 📌 Principais resultados:
- O modelo apresenta boa capacidade de capturar a tendência do NPS
- Variáveis mais relevantes:
  - 🔻 delivery_delay_days
  - 🔻 complaints_count
  - 🔻 customer_service_contacts
  - 🔺 csat_internal_score

---

## 🚀 Como Reproduzir os Resultados

###  1. Clonar o repositório
```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

###  2. Criar Ambiente Virtual
```bash
python -m venv venv
venv\Scripts\activate
```

###  3. Instalar Dependências
```bash
pip install -r requirements.txt
```