# 📊 Previsão de Detratores e Otimização de Retenção em E-commerce

Este projeto vai além da análise de NPS, propondo um **motor de decisão orientado por dados**, capaz de antecipar o risco de insatisfação e priorizar ações com impacto direto na receita.

---

## 🎯 Objetivo do Projeto

O objetivo é identificar os fatores que impactam a satisfação dos clientes e desenvolver um modelo capaz de **prever a probabilidade de um cliente se tornar detrator** com base em dados operacionais.

Com isso, a solução permite que a empresa:

- Antecipe clientes com risco de insatisfação  
- Identifique os principais drivers da experiência  
- Priorize clientes com maior impacto financeiro  
- Direcione ações de retenção de forma estratégica  

---

## 📂 Base de Dados

Dataset com informações da jornada do cliente em um e-commerce:

### 🔢 Variáveis numéricas
- `nps`  
- `atraso_entrega_dias`  
- `contatos_atendimento`  
- `numero_reclamacoes`  
- `valor_pedido`  
- `quantidade_itens`  
- `valor_desconto`  
- `parcelas_pagamento`  
- `tempo_entrega_dias`  
- `idade_cliente`  
- `tempo_cliente_meses`  

### 🏷️ Variável categórica
- `regiao_cliente`

### 🚫 Variáveis removidas (evitar data leakage)
- `csat_interno`  
- `recompra_30_dias`  

---

## 🔍 Principais Insights (EDA)

- Alta concentração de **clientes detratores (~74%)**
- Principais fatores de insatisfação:
  - 🚚 Atraso na entrega  
  - 📞 Alto número de contatos com atendimento  
  - ⚠️ Reclamações recorrentes  

- Foi identificado um **ponto crítico (~2 dias de atraso)**, a partir do qual a satisfação do cliente cai significativamente.

👉 Insight-chave: a experiência do cliente é altamente sensível a falhas operacionais.

---

## 🧠 Modelagem Preditiva

O problema foi tratado como **classificação**, com foco em identificar clientes com risco de insatisfação:

- **Target:**  
  - `1` → Detrator (NPS ≤ 6)  
  - `0` → Não detrator  

### 🤖 Modelos testados:

- Logistic Regression  
- Decision Tree  
- Random Forest  
- Gradient Boosting  
- XGBoost  
- LightGBM  

---

## 🏆 Modelo Final

**Gradient Boosting Classifier (tunado)**

### Motivos:

- Melhor equilíbrio entre **precision e recall**
- Alto **recall para detratores (~94%)**
- Melhor desempenho geral (F1-score)
- Boa estabilidade (cross-validation)

👉 Foco estratégico: identificar o máximo possível de clientes em risco.

---

## 🔧 Feature Engineering

Features criadas com base nos insights do EDA:

- `atraso_critico` → atraso ≥ 2 dias  
- `problema_complexo` → múltiplos contatos + alta resolução  
- `reclamacao_recorrente` → volume elevado de reclamações  

👉 Essas variáveis tornam o modelo mais interpretável e alinhado ao negócio.

---

## 🔁 Validação do Modelo

Cross-validation (5 folds):

- Accuracy: **~0.83**  
- Recall (detratores): **~0.94**  
- F1-score: **~0.89**  
- ROC-AUC: **~0.87**  

👉 Modelo robusto, com forte capacidade de identificar clientes em risco.

---

## 🚀 Geração de Valor (Diferencial do Projeto)

O modelo foi transformado em um **motor de decisão de negócio**.

---


### 1️⃣ Probabilidade de Risco

```python
prob_detrator = modelo.predict_proba(X)[:,1]
```
- Quanto maior a probabilidade → maior o risco  
- Permite priorização baseada em dados  

---

### 2️⃣ Segmentação de Clientes

- 🟢 **Seguro**  
- 🟡 **Neutro**  
- 🟠 **Atenção**  
- 🔴 **Crítico**  

👉 Identificação rápida de clientes que exigem ação  

---

### 3️⃣ Estratégia de Ação

- 🔴 **Crítico** → 40% de desconto  
- 🟠 **Atenção** → 20% de desconto  
- 🟡 **Neutro** → 10% de desconto  
- 🟢 **Seguro** → sem ação  

👉 Ações deixam de ser genéricas e passam a ser direcionadas  

---

###  4. Prioridade Financeira

```python
prioridade = prob_detrator * valor_pedido
```

Permite:

- Identificar clientes com maior impacto financeiro  
- Priorizar ações com maior retorno  
- Otimizar o uso de incentivos  

👉 **Insight-chave:**

> Não basta identificar quem está em risco — é preciso priorizar quem impacta mais a receita.

---

## 📈 Resultado

O sistema permite:

- Antecipar insatisfação  
- Priorizar clientes críticos  
- Reduzir desperdício de incentivos  
- Maximizar retenção  

---

## 🖥️ Aplicação (Streamlit)

Foi desenvolvida uma aplicação interativa para uso prático pelo negócio.

### Funcionalidades:

- Upload de CSV  
- Previsão de risco de detrator  
- Segmentação automática  
- Sugestão de ações  
- Download dos resultados  

👉 Interface simples e orientada à decisão  

---

## 🏁 Conclusão

O projeto evolui de uma análise exploratória para um **sistema de decisão orientado por risco e valor**, permitindo:

- Antecipar problemas na experiência  
- Priorizar clientes com maior impacto financeiro  
- Otimizar recursos  
- Aumentar retenção  

👉 Transformando dados em decisões com impacto real no negócio.
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
