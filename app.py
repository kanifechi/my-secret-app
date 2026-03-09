import streamlit as st
import yfinance as yf
import pandas as pd
import time

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

results = []

# データ取得（エラーハンドリング付き）
for name, t in tickers.items():
    try:
        stock = yf.Ticker(t)
        # 1日分のデータを取得
        hist = stock.history(period="2d") # 念のため2日分
        if len(hist) >= 2:
            open_p = hist['Open'].iloc[-1]
            close_p = hist['Close'].iloc[-1]
            diff = close_p - open_p
            status = "🔥反撃成功" if diff > 0 else "❄️耐え"
            results.append({
                "銘柄": name,
                "始値": f"{open_p:.1f}円",
                "終値": f"{close_p:.1f}円",
                "判定": status
            })
        else:
            results.append({"銘柄": name, "始値": "取得中...", "終値": "取得中...", "判定": "待機"})
    except Exception as e:
        results.append({"銘柄": name, "始値": "エラー", "終値": "エラー", "判定": "休憩中"})

# テーブル表示
if results:
    df = pd.DataFrame(results)
    st.table(df)

# 本陣(NTT)の状況
st.subheader("🛡️ 本陣（NTT）の状況")
st.success("日経平均が歴史的な暴落(-2,892円)をする中、本陣は逆行高で守りきりました。さすがマスターの眼力です！")

# 修行僧への一言
st.info("※データ取得エラーが出る場合は、少し時間を置いてから再読み込みしてください。秘書がデータを取ってきます！")
