# 🔐 Simulação de Segurança — Tokens de 6 Dígitos

Este projeto é uma aplicação interativa desenvolvida em **Python + Streamlit** para demonstrar, de forma visual e prática, como funciona a probabilidade de um invasor adivinhar um **token de 6 dígitos** utilizando até **3 tentativas por token**.

A simulação permite visualizar token por token (modo completo) ou rodar rapidamente sem exibir detalhes (modo rápido).  
Ideal para fins **educacionais**, demonstrações de **segurança**, conteúdos para **aulas**, **reels** e workshops.

---

## 🌐 Acesse o projeto online

🔗 **Versão web (Streamlit Cloud):**  
👉 https://security-tokens.streamlit.app/

---

## 🚀 Funcionalidades

### ✔️ Geração de tokens reais  
Cada token é composto por 6 dígitos aleatórios.

### ✔️ Tentativas de ataque  
Para cada token, são geradas 3 tentativas independentes.

### ✔️ Dois modos de simulação
- **Modo detalhado**: exibe token por token e todas as tentativas.  
- **Modo rápido**: executa silenciosamente, ideal para grandes volumes.

### ✔️ Estatísticas finais
Ao final da simulação, são exibidos:
- Probabilidade **simulada**
- Probabilidade **teórica**
- Total de tokens gerados
- Total de tokens quebrados
- Total de tokens protegidos

---

## 🛠️ Tecnologias utilizadas

- **Python 3.8+**
- **Streamlit**
- Bibliotecas padrão do Python:
  - `random`
  - `time`
