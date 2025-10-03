import streamlit as st
import MetaTrader5 as mt5

st.title("Dashboard Trading")

col1, col2 = st.columns(2)

with col1:
    if st.button("Conectar MT5"):
        st.info("Funcionalidade em desenvolvimento")

with col2:
    if st.button("Ver Performance"):
        st.info("Performance: $490.00 | Trades: 15")

st.markdown("---")
st.subheader("Posições Ativas:")
st.write("EURUSD 0.02L | EURUSD 0.025")
