import MetaTrader5 as mt5
if mt5.initialize():
    positions = mt5.positions_get()
    if positions:
        print("📊 POSIÇÕES ABERTAS:")
        for pos in positions:
            print(f"• {pos.symbol} | Volume: {pos.volume} | Lucro: ${pos.profit:.2f}")
    else:
        print("✅ Nenhuma posição aberta")
    mt5.shutdown()
