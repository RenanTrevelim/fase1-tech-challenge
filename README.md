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

A análise exploratória evidenciou uma forte concentração de clientes detratores (~74%), indicando um cenário crítico de experiência.

Os principais fatores associados à insatisfação foram:

- 🚚 Atraso na entrega  
- 📞 Alto número de contatos com atendimento  
- ⚠️ Reclamações recorrentes  

Foi identificado um **ponto de ruptura a partir de 2 dias de atraso**, onde a satisfação passa a cair de forma mais acentuada.

👉 Insight-chave:

A insatisfação não é aleatória — ela está diretamente ligada a falhas operacionais recorrentes, especialmente relacionadas à logística e resolução de problemas.
---

## 🧠 Modelagem Preditiva

O problema foi tratado como **classificação**, com o objetivo de identificar antecipadamente clientes com risco de insatisfação.

Mais do que prever o NPS, o modelo foi desenvolvido para apoiar decisões de negócio, permitindo atuar antes que a insatisfação aconteça.

👉 Foco principal:
Maximizar a identificação de clientes detratores (recall da classe 1), reduzindo o risco de perda de clientes sem ação preventiva.

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

O modelo foi escolhido por apresentar o melhor equilíbrio entre desempenho e capacidade de identificação de clientes em risco.

Principais pontos:

- Alto recall para detratores (~94%)  
- Melhor F1-score entre os modelos  
- Boa estabilidade na validação cruzada  

👉 Decisão estratégica:

O modelo prioriza a identificação de clientes insatisfeitos, mesmo ao custo de alguns falsos positivos, pois o impacto de não agir sobre um cliente em risco é maior do que agir desnecessariamente.
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

A segmentação dos clientes permite definir ações proporcionais ao nível de risco:

- 🔴 Crítico → ações mais agressivas (ex: incentivos maiores)  
- 🟠 Atenção → ações intermediárias  
- 🟡 Neutro → ações leves  
- 🟢 Seguro → sem necessidade de ação  

Essa abordagem evita desperdício de recursos e direciona esforços para onde o impacto é maior.

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

## 💰 Impacto financeiro estimado

A partir da probabilidade de cada cliente se tornar detrator, foi construída uma métrica de risco financeiro, combinando:

- Probabilidade de churn  
- Valor do pedido  

Isso permitiu estimar o valor financeiro em risco por cliente e por segmento.

Com base nessa análise, foi identificado que:

- A maior parte do risco financeiro está concentrada nos clientes críticos  
- Ações direcionadas nesses clientes geram maior retorno potencial  

Considerando um cenário conservador de recuperação:

💰 Impacto financeiro estimado: **~R$ 40 mil em valor recuperável**

👉 Insight-chave:

O modelo não apenas identifica risco, mas permite quantificar o valor que pode ser preservado com ações preventivas.

---

### 📊 Retorno sobre investimento (ROI)

Para avaliar a viabilidade financeira das ações de retenção, foi realizada uma simulação de ROI considerando diferentes cenários de custo operacional.

Como os custos podem variar (incentivos, atendimento e execução das ações), foram definidos três cenários:

- **Conservador (R$ 30 mil):** maior custo de implementação  
- **Moderado (R$ 20 mil):** cenário intermediário  
- **Otimista (R$ 10 mil):** operação mais eficiente  

Com base no impacto financeiro estimado (~R$ 40 mil), os resultados foram:

- **Conservador:** ROI de ~34%  
- **Moderado:** ROI de ~102%  
- **Otimista:** ROI de ~303%  

### Interpretação

- Mesmo em um cenário conservador, as ações apresentam retorno positivo  
- No cenário moderado, o investimento se paga e gera valor adicional  
- No cenário otimista, o retorno se torna significativamente elevado  

### Insight principal

A priorização de clientes com base em risco e valor financeiro permite maximizar o retorno das ações, tornando a estratégia mais eficiente do que abordagens genéricas.

Essa abordagem transforma o modelo em uma ferramenta de decisão, conectando Machine Learning diretamente ao resultado financeiro do negócio.

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
<img width="1905" height="836" alt="Captura de tela 2026-04-23 202111" src="https://github.com/user-attachments/assets/0946683b-321a-4390-9617-9c96056afcd0" />
<img width="1906" height="855" alt="Captura de tela 2026-04-23 202131" src="https://github.com/user-attachments/assets/db555231-6328-4f5b-ac05-ae9e02929dca" />


---

## 🏁 Conclusão


O projeto evolui de uma análise exploratória para um sistema de decisão orientado por risco e valor.

Mais do que prever insatisfação, a solução permite:

- Identificar clientes em risco com antecedência  
- Priorizar ações com base em impacto financeiro  
- Otimizar a alocação de recursos  
- Reduzir perdas e aumentar retenção  

👉 Resultado:

Machine Learning aplicado diretamente à tomada de decisão, conectando dados, operação e impacto financeiro real.
---

## Reproduzir no Docker

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

### 3. Execute o Docker
```bash
docker build -t fase1-tech-challenge .
docker run -p 8501:8501 fase1-tech-challenge
```

## Reproduzir no Streamlit

### 1. Baixar as Dependências
```bash
pip install -r requirements.txt
```

### 2. Executar o Streamlit
```bash
streamlit run main.py
```
