import streamlit as st
import MetaTrader5 as mt5
import pandas as pd

st.set_page_config(page_title="Robô Luxo", page_icon="📈", layout="wide")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("🤖 Controles do Robô")

if st.sidebar.button("▶️ Iniciar Robô"):
    st.sidebar.success("Robô iniciado!")

if st.sidebar.button("⏹️ Parar Robô"):
    st.sidebar.warning("Robô parado!")

# --- MAIN DASHBOARD ---
st.title("🤖 Robô Luxo - AvaTrade MT5")

if st.button("🔄 Atualizar Dados MT5"):
    try:
        if mt5.initialize():
            account = mt5.account_info()
            st.success("✅ Conectado ao MT5!")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("💰 Saldo", f"${account.balance:,.2f}")
            col2.metric("📈 Equity", f"${account.equity:,.2f}") 
            col3.metric("🎯 Lucro", f"${account.profit:,.2f}")
            
            mt5.shutdown()
        else:
            st.error("❌ Falha ao conectar ao MT5")
    except Exception as e:
        st.error(f"❌ Erro: {e}")

# Posições atuais
st.sidebar.subheader("📊 Posições Atuais")
st.sidebar.write("EURUSD | Volume: 0.02 | Lucro: $1.19")
st.sidebar.write("EURUSD | Volume: 0.02 | Lucro: $-1.43")
