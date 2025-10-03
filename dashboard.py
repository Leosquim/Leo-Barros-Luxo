import streamlit as st
import MetaTrader5 as mt5

# Configuração simples e limpa
st.set_page_config(page_title="Robô Luxo", layout="centered")

st.title("🤖 Robô Luxo Trading")
st.markdown("---")

# Controles simples
col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 Atualizar Dados MT5", type="primary"):
        try:
            if mt5.initialize():
                acc = mt5.account_info()
                st.success(f"Saldo: ${acc.balance:.2f} | Equity: ${acc.equity:.2f}")
                mt5.shutdown()
        except:
            st.error("Erro ao conectar")

with col2:
    if st.button("📊 Ver Performance"):
        st.info("Performance: $490.00 | Trades: 15")

st.markdown("---")
st.write("**Posições Ativas:** EURUSD 0.02L | EURUSD 0.02S")

