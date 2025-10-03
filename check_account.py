import MetaTrader5 as mt5
if mt5.initialize():
    acc = mt5.account_info()
    print(f"💰 CONTA: {acc.login}")
    print(f"🏦 SERVIDOR: {acc.server}") 
    print(f"📊 LUCRO ATUAL: ${acc.profit:.2f}")
    mt5.shutdown()
