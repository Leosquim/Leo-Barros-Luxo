import MetaTrader5 as mt5
if mt5.initialize():
    print("✅ Conectado ao MT5!")
    print(f"📊 Conta: {mt5.account_info().login}")
    mt5.shutdown()
else:
    print("❌ Falha na conexão - Verifique se o MT5 está aberto")
