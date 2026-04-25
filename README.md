# 📊 Previsão de Detratores e Otimização de Retenção em E-commerce

Projeto desenvolvido no contexto do Tech Challenge (Fase 1), com foco na análise de satisfação do cliente (NPS) em um cenário de e-commerce.

---

## 🎯 Objetivo do Projeto

O objetivo deste projeto é identificar os fatores que impactam a satisfação dos clientes em um e-commerce e desenvolver uma abordagem baseada em dados para **antecipar clientes com risco de insatisfação (detratores)**.

A partir disso, busca-se:

- Entender os principais drivers do NPS
- Identificar padrões de comportamento dos clientes
- Apoiar decisões de negócio com base em dados
- (Opcional) Desenvolver um modelo preditivo para antecipação de detratores

---

## 📂 Descrição da Base de Dados

O dataset contém informações relacionadas à jornada do cliente em um e-commerce, incluindo dados de pedidos, logística e atendimento.

As variáveis podem ser agrupadas da seguinte forma:

### 👤 Cliente
- `customer_age` → idade do cliente  
- `customer_region` → região  
- `customer_tenure_months` → tempo de relacionamento  

### 🛒 Pedido
- `order_value` → valor do pedido  
- `items_quantity` → quantidade de itens  
- `discount_value` → desconto aplicado  
- `payment_installments` → número de parcelas  

### 🚚 Logística
- `delivery_time_days` → tempo de entrega  
- `delivery_delay_days` → atraso na entrega  
- `freight_value` → valor do frete  
- `delivery_attempts` → tentativas de entrega  

### 📞 Atendimento
- `customer_service_contacts` → contatos com atendimento  
- `resolution_time_days` → tempo de resolução  
- `complaints_count` → número de reclamações  

### 📊 Satisfação
- `nps_score` → nota NPS (0 a 10)  
- `csat_internal_score` → score interno (removido do modelo)  
- `repeat_purchase_30d` → recompra (removido do modelo)  

👉 Variáveis como `csat_internal_score` e `repeat_purchase_30d` foram removidas da modelagem para evitar **data leakage**.

---

## 🧠 Metodologia Utilizada

O projeto foi desenvolvido em etapas:

### 1. Entendimento do problema
Análise do problema de negócio, focando na dificuldade da empresa em antecipar a insatisfação dos clientes antes da coleta do NPS.

---

### 2. Análise Exploratória de Dados (EDA)

Foram investigados padrões e relações entre variáveis com foco em negócio.

Principais análises realizadas:

- Distribuição do NPS  
- Relação entre atraso de entrega e satisfação  
- Impacto de contatos com atendimento  
- Frequência de reclamações  
- Identificação de pontos críticos na experiência  
- Foi identificado um ponto de ruptura a partir de aproximadamente 2 dias de atraso, onde a probabilidade de insatisfação aumenta de forma significativa.

👉 A análise mostrou que a insatisfação está fortemente associada a:

- Atrasos na entrega  
- Alto número de contatos com atendimento  
- Reclamações recorrentes  

---

### 3. Definição da variável alvo

A variável alvo foi definida a partir do NPS:

- Detrator: NPS ≤ 6  
- Não detrator: NPS > 6  

Essa transformação permitiu tratar o problema como **classificação**, focando na identificação de clientes em risco.

---

### 4. Modelagem Preditiva

Foi desenvolvido um modelo de classificação para prever a probabilidade de um cliente se tornar detrator.

Etapas:

- Separação treino/teste  
- Teste de múltiplos algoritmos:
  - Logistic Regression  
  - Decision Tree  
  - Random Forest  
  - Gradient Boosting  
  - XGBoost  
  - LightGBM  

- Seleção do modelo final: **Gradient Boosting**

Critério de avaliação:

- Recall para detratores (prioritário)
- F1-score
- ROC-AUC

---

### 5. Feature Engineering

Criação de variáveis baseadas em insights do EDA:

- `atraso_critico` → atraso ≥ 2 dias  
- `problema_complexo` → múltiplos contatos + tempo de resolução  
- `reclamacao_recorrente` → alto número de reclamações  

---

### 6. Aplicação do Modelo

O modelo pode ser utilizado para:

- Identificar clientes com risco de insatisfação  
- Priorizar ações de retenção  
- Apoiar decisões operacionais  

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

👉 Resultado: Machine Learning aplicado diretamente à tomada de decisão, conectando dados, operação e impacto financeiro real.

---

## ▶️ Como Reproduzir os Resultados

###  Clonar o repositório
```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

## 🐳 Execute Com Docker(Recomendado)
```bash
docker build -t fase1-tech-challenge .
docker run -p 8501:8501 fase1-tech-challenge
```

## 💻 Execução Local (Sem Docker)

### 1. Criar ambiente Virtual
```bash
python -m venv env
env\Scripts\activate   # Windows
# source env/bin/activate  # Linux/Mac
```

### 2. Baixar as Dependências
```bash
pip install -r requirements.txt
```

### 3. Executar o Streamlit
```bash
streamlit run main.py
```
