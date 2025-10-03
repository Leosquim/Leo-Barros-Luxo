import MetaTrader5 as mt5
if mt5.initialize():
    print("✅ CONECTADO AO MT5!")
    acc = mt5.account_info()
    print(f"Conta: {acc.login} | Corretora: {acc.company}")
    mt5.shutdown()
else:
    print("❌ FALHA - Verifique se o MT5 está ABERTO")
