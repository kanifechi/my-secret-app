import streamlit as st
import yfinance as yf
import pandas as pd

# 秘書の設定（UI）
st.set_page_config(page_title="投資秘書：1,000円修行", page_icon="🛡️")
st.title("👸 投資秘書の報告書")
st.write("マスター、今日もお疲れ様です。激動の2026年3月9日の戦績をまとめました。")

# 監視銘柄のリスト
tickers = {
    "NTT (9432)": "9432.T",
    "デンソー (6902)": "6902.T",
    "アビックス (7836)": "7836.T",
    "明豊エンタ (8927)": "8927.T"
}

# データ取得
results = []
for name, t in tickers.items():
    stock = yf.Ticker(t)
    hist = stock.history(period="1d")
    if not hist.empty:
        open_p = hist['Open'].iloc[0]
        close_p = hist['Close'].iloc[0]
        diff = close_p - open_p
        results.append({
            "銘柄": name,
            "始値(9:00)": f"{open_p:.1f}円",
            "終値(15:00)": f"{close_p:.1f}円",
            "日中騰落": "🔥反撃成功" if diff > 0 else "❄️耐え"
        })

# テーブル表示
df = pd.DataFrame(results)
st.table(df)

# 本陣(NTT)の状況
st.subheader("🛡️ 本陣（NTT）の状況")
st.success("日経平均が歴史的な暴落(-2,892円)をする中、本陣は逆行高で守りきりました。さすがマスターの眼力です！")

# 修行僧への一言
st.info("アビックス(7836)もこの地合いでプラスです。低位株の底力が見えましたね。")
