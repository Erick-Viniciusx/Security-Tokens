import streamlit as st
import random
import time 

def gerar_token():
    return "".join(str(random.randint(0, 9)) for _ in range(6))

def gerar_tentativa():
    return "".join(str(random.randint(0, 9)) for _ in range(6))

# Inicializando contadores persistentes
if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0

if "acertos" not in st.session_state:
    st.session_state.acertos = 0

st.title("🔐 Simulação — Segurança de Tokens de 6 dígitos")
qtd_tokens = st.number_input("Quantos tokens deseja simular?", 1, 1000000, 5)

cols1, cols2 = st.columns([0.5,0.5]) 

with cols1:
    btn = st.button("Gerar tokens")

with cols2:
    btn2 = st.button("Gerar rápido")

if btn:
    with st.spinner("⏳Processando..."):
        
        st.session_state.total_tokens = 0
        st.session_state.acertos = 0

        # containers que serão reutilizados
        token_box = st.empty()
        tentativa_box = st.empty()
        resultado_box = st.empty()

        for i in range(qtd_tokens):

            token_real = gerar_token()
            acertou = False

            st.session_state.total_tokens += 1

            # mostra token real
            token_box.markdown(f"### 🔹 Token #{i+1} — **{token_real}**")

            tentativas_texto = "**Tentativas do invasor:**\n"

            for t in range(3):
                tentativa = gerar_tentativa()
                tentativas_texto += f"- Tentativa {t+1}: `{tentativa}`\n"


                if tentativa == token_real:
                    acertou = True

            tentativa_box.markdown(tentativas_texto)

            # feedback
            if acertou:
                st.session_state.acertos += 1
                resultado_box.error("🚨 Hacker conseguiu acertar o token!")
                with st.spinner("⚠️ Hacker acertou! Analisando..."):
                    time.sleep(5)
            else:
                resultado_box.success("🟢 Token seguro — nenhuma tentativa foi bem-sucedida.")

        
        st.subheader("📊 Resultado geral da simulação")
        prob_simulada = st.session_state.acertos / st.session_state.total_tokens
        st.write(f"📊 Probabilidade simulada: {prob_simulada:.8f}")
        prob_teorica = 1 - (999999/1000000)**3
        st.write(f"📘 Probabilidade teórica: {prob_teorica:.8f}")
        st.write(f"🔢 Tokens simulados: **{st.session_state.total_tokens}**")
        st.write(f"❗ Tokens quebrados: **{st.session_state.acertos}**")
        st.write(f"🛡️ Tokens protegidos: **{st.session_state.total_tokens - st.session_state.acertos}**")

    st.success("✅ Processamento Concluído...")

elif btn2:
    with st.spinner("⏳Processando..."):
        st.session_state.total_tokens = 0
        st.session_state.acertos = 0

        token_box = st.empty()
        tentativa_box = st.empty()
        resultado_box = st.empty()

        for i in range(qtd_tokens):

            token_real = gerar_token()
            acertou = False

            st.session_state.total_tokens += 1

        

            for t in range(3):
                tentativa = gerar_tentativa()

                if tentativa == token_real:
                    acertou = True

            # feedback
            if acertou:
                st.session_state.acertos += 1
                resultado_box.error("🚨 Hacker conseguiu acertar o token!")
                with st.spinner("⚠️ Hacker acertou! Analisando..."):
                    token_box.markdown(f"### 🔹 Token #{i+1} — **{token_real}**")
                    tentativas_texto = f"- Tentativa {t+1}: `{tentativa}`\n"
                    tentativa_box.markdown(tentativas_texto)
                    time.sleep(5)


        st.subheader("📊 Resultado geral da simulação")
        prob_simulada = st.session_state.acertos / st.session_state.total_tokens
        st.write(f"📊 Probabilidade simulada: {prob_simulada:.8f}")
        prob_teorica = 1 - (999999/1000000)**3
        st.write(f"📘 Probabilidade teórica: {prob_teorica:.8f}")
        st.write(f"🔢 Tokens simulados: **{st.session_state.total_tokens}**")
        st.write(f"❗ Tokens quebrados: **{st.session_state.acertos}**")
        st.write(f"🛡️ Tokens protegidos: **{st.session_state.total_tokens - st.session_state.acertos}**")  
         
    st.success("✅ Processamento Concluído...")
